
def unique( c_i, C):
	e_unique = C[c_i].event_set
	for c_j in C:
		if c_j != ci:
			e_unique = e_unique - C[c_j].event_set

	return e_unique

#retrieves the events from E given by the indicies, indicies. 
#It creates a shallow copy which when modified, modifies E as well
def getEventsSubsetShallow(E, indicies):
	E_p = []
	for e_i in indicies:
		E_p.append( E[e_i] )
	return E_p

#requires baae_P
def selectEventPlacement(P, C, e_i):
	max_val = -1
	max_c = None
	for c_i in range(len(C)):
		event = C[c_i].E[e_i] 
		val = placementValue(event, P)
		if val > max_val:
			max_val = val
			max_c = c_i
	#max_c contains the cluster with best event placement for e_i
	return C[max_c].E[e_i]

def placementValue(event, P):
	if event.day == None:
		return -1
	sum = 0
	for p_i in event.invited:
		if event.weight > P[p_i].SCHEDULE[event.day][event.slot]:
			sum = event.weight - P[p_i].SCHEDULE[event.day][event.slot]
	return sum

def evaluateClusterPlacements(E, P, C):
	for e_i in range(len(E)):
		E[e_i] = selectEventPlacement(P, C, e_i)

# def getEventsSubsetDeep(E, indicies):
# 	E_p = []
# 	for e_i in indicies:
# 		E_p.append( copy.deepcopy(E[e_i]) )
# 	return E_p