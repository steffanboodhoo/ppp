def totalSum(P, utl):
	sum = 0
	for d in range(utl.DAY):
		for t in range(utl.SLOT):
			for person in P:
				sum += person.SCHEDULE[d][t]

	return sum