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
		depts[i] = {'P':[]} #each department's population, property P; list
		for p in range(utl.PER_DEPT):
			person = Person(id=len(P), dept=i) #creating Person
			P.append(person)#adding Person to population P
			depts[i]['P'].append(person.id)#adds index of new person to dept population


	
	# for i in range(len(depts)):
	# 	print depts[i]
	return [P,depts]



def genE(utl, P, depts):
	utl = Utils.Instance()
	E = []

	#TYPE A
	print utl.DEPT_EVENTS_A
	for i in range(utl.DEPT_COUNT):
		for j in range(utl.DEPT_EVENTS_A):
			# print j
			# print len(E)
			event = Event(id=len(E), weight=random.randint(utl.VAL+1,10))
			event.inviteA( P=P, dept=depts[i])
			E.append(event)

	return E

if __name__ == '__main__':
	print 'hi'


	