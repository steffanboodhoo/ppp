from models import *

def extendEvents(P, depts, K):
	k = k/len(depts)
	#for each department
	for d_i in len(range(depts)):
		#for each new event being added to department d_i
		for e_i_t in range(k):
			e_i = len(P) + e_i_t
			event = Event(id=e_i, weight=random.randint(utl.VAL+1,10))
			event.inviteA( P=P, dept=depts[d_i])
			E.append(event)

