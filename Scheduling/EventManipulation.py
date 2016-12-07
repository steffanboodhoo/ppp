#P is the population of people
def findPlace(event, P, utl):
	max_sum = 0
	max_day = 0
	max_slot = 0
	for d in range(utl.DAY): #for each day
		for t in range(utl.SLOT): # for each slot
			diff = 0
			for p_i in event.invited: # p_i is person's index or id 
				if event.weight > P[p_i].SCHEDULE[d][t]:
					#add what the difference WOULD be 
					diff += event.weight - P[p_i].SCHEDULE[d][t]
			if diff > max_sum :
				max_sum = diff
				max_day = d
				max_slot = t

	event.day = max_day
	event.slot = max_slot
	return [max_day, max_slot]

def placeEvent(event, P):
	for p_i in event.invited:
		if event.weight > P[p_i].SCHEDULE[event.day][event.slot]:
			P[p_i].SCHEDULE[event.day][event.slot] = event.weight


#E is the set of events, and P is the set of persons, 
#base_P is the unmodified set of persons
def removeEvent(e_i, E, P, base_P):
	event = E[e_i]
	for p_i in event.invited:
		person = P[p_i]
		#return person's slot to base weight before any events
		person.SCHEDULE[event.day][event.slot] = base_P[p_i].SCHEDULE[event.day][event.slot]

		#try placing other events that have the same day & slot
		#conditions; not same event, same day, same slot, event weight bigger than day,slot weight
		for e_j in person.events:
			#not same event
			if e_j != e_i \
				and E[e_i].day == E[e_j].day \
				and E[e_i].slot == E[e_j].slot \
				and E[e_j].weight > person.SCHEDULE[event.day][event.slot]:
				person.SCHEDULE[event.day][event.slot] = E[e_j].weight

def totalSum(P, utl):
	sum = 0
	for d in range(utl.DAY):
		for t in range(utl.SLOT):
			for person in P:
				sum += person.SCHEDULE[d][t]

	return sum
	
def TS(E, P, utl):
	for event in E:
		[max_day, max_slot] = findPlace(event, P, utl)
		placeEvent(event, P)

def CA(E, P, utl, base_P):
	for event in E:
		removeEvent(event.id, E, P, base_P)
		[max_day, max_slot] = findPlace(event, P, utl)
		placeEvent(event,P)


if __name__ == '__main__':
	print' meh'