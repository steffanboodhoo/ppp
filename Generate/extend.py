from models import *

def extendEvents(E, P, depts, k):
	utl = Utils.Instance()
	k = k/len(depts)
	print 'k',k
	#for each department
	for d_i in range(len(depts)):
		#for each new event being added to department d_i
		for e_i_t in range(k):
			# e_i = len(P) + e_i_t
			event = Event(id=len(E), weight=random.randint(utl.VAL+1,10))
			event.inviteA( P=P, dept=depts[d_i])
			E.append(event)

		#each time we add k events to a dept we need to record it
		utl.DEPT_EVENTS_A  = utl.DEPT_EVENTS_A  + k