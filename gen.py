import random
from cluster import cluster
from pprint import pprint
from models import Person
from models import Event
from Config import utils 
from pprint import pprint
from Scheduling import Aggregates as aggr
from Scheduling import EventManipulation as evman
import copy
import random

def test():
	#Event space
	events = range(1,11)
	P = []
	for i in range(10):
		P.append(random.sample(events,random.randint(3,5)))
	return P


def genP(utl):
	P = []
	#creating departments
	depts = [0] * utl.DEPT_COUNT

	#for each department
	for i in range(utl.DEPT_COUNT):
		depts[i] = {'P':[]} #each department's population, property P; list
		for p in range(utl.PER_DEPT):
			person = Person(utils=utl, id=len(P), dept=i) #creating Person
			P.append(person)#adding Person to population P
			depts[i]['P'].append(person.id)#adds index of new person to dept population


	
	# for i in range(len(depts)):
	# 	print depts[i]
	return [P,depts]



def genE(utl, P, depts):
	E = []

	#TYPE A
	for i in range(utl.DEPT_COUNT):
		for j in range(utl.DEPT_EVENTS_A):
			event = Event(id=len(E), weight=random.randint(utl.VAL+1,10))
			event.inviteA(depts[i], utl, P)
			E.append(event)
	return E

if __name__ == '__main__':
	
	# P = test()
	# k=3
	# centroids = cluster.select_centroids(P,k)
	# print centroids
	# clusters = cluster.place_points(P,centroids)
	# pprint(clusters)
	utl = utils()
	[P,depts] = genP(utl)
	base_P = copy.deepcopy(P)
	E = genE(utl, P, depts)
	# for p in P:
	# 	print p
	base =  aggr.totalSum(P=P,utl=utl)
	evman.TS(E=E, P=P, utl=utl)
	ts = aggr.totalSum(P=P, utl=utl)
	evman.CA(E=E, P=P, utl=utl, base_P=base_P)
	ca = aggr.totalSum(P=P, utl=utl)
	print ca - ts