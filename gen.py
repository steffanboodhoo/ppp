import random
from Clus import core, group
from pprint import pprint
from models import *
from Config import utils 
from pprint import pprint
from Scheduling import Aggregates as aggr
from Scheduling import EventManipulation as evman

import copy
import random

utl = utils()
def test():
	#Event space
	events = range(1,11)
	P = []
	for i in range(10):
		P.append(random.sample(events,random.randint(3,5)))
	return P


def genP():
	P = []
	#creating departments
	depts = [0] * utl.DEPT_COUNT

	#for each department
	for i in range(utl.DEPT_COUNT):
		depts[i] = {'P':[]} #each department's population, property P; list
		for p in range(utl.PER_DEPT):
			person = Person(id=len(P), dept=i) #creating Person
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
			event.inviteA( P=P, dept=depts[i])
			E.append(event)
	return E

if __name__ == '__main__':
	
	# P = test()
	# k=3
	# centroids = cluster.select_centroids(P,k)
	# print centroids
	# clusters = cluster.place_points(P,centroids)
	# pprint(clusters)
	# utl = utils()
	[P,depts] = genP()
	base_P = copy.deepcopy(P)
	E = genE(utl, P, depts)
	C = core.initClusters(P, utl.K, depts)
	C = core.placePeople(P,C)
	for c in C:
		c.scheduleClusterP1( copy.deepcopy(E), copy.deepcopy(P), base_P)

	for e_i in range(len(E)):
		for c in C:
			print c.E[e_i]
		# print E[e_i]
		print '\n'

	# evman.TS( E=E, P=P, utl=utl)
	# print aggr.totalSum(P=P,utl=utl),'\n'
	group.evaluateClusterPlacements(E, P, C)
	for e in E:
		evman.placeEvent(e, P)

	# for c in C:
	# 	print c
	# C[0].recalculateCentroid(P,3)
	# base =  aggr.totalSum(P=P,utl=utl)
	# evman.TS(E=E, P=P, utl=utl)
	# ts = aggr.totalSum(P=P, utl=utl)
	# evman.CA(E=E, P=P, utl=utl, base_P=base_P)
	# ca = aggr.totalSum(P=P, utl=utl)
	# print ca - ts
	