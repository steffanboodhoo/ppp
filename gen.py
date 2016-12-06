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
	
	[P,depts] = genP()
	base_P = copy.deepcopy(P)
	E = genE(utl, P, depts)
	C = core.initClusters(P, utl.K, depts)
	C = core.placePeople(P,C)
	for c in C:
		c.scheduleClusterP1( copy.deepcopy(E), copy.deepcopy(P), base_P)


	print aggr.totalSum(P=P,utl=utl)

	group.evaluateClusterPlacements(E, P, C)
	for e in E:
		evman.placeEvent(e, P)

	print aggr.totalSum(P=P,utl=utl)

	