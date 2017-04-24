import copy
import random
from pprint import pprint

from Config import Utils 
from models import *



def genP():
	utl = Utils.Instance()
	P = []
	#creating departments
	depts = [0] * utl.DEPT_COUNT

	#for each department
	for i in range(utl.DEPT_COUNT):
		depts[i] = [] #each department's population; list containing id's referencing actual population 

		#for each person in the department
		for p in range(utl.PER_DEPT):
			#Create Person
			person = Person(id=len(P), dept=i) 
			#Add person to population
			P.append(person)
			#Add's reference of this person to current department
			depts[i].append(person.id)

	return [P,depts]



def genE(utl, P, depts):
	utl = Utils.Instance()
	E = []

	#TYPE A
	for i in range(utl.DEPT_COUNT):
		for j in range(utl.DEPT_EVENTS_A):
			event = Event(id=len(E), weight=random.randint(utl.VAL+1,10))
			event.inviteA( P=P, dept=depts[i])
			E.append(event)

	return E

if __name__ == '__main__':
	print 'hi'


	