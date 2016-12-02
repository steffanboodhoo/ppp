
class SimpleSol(object):

	def __init__(self,utils):
		self.utl = utils
		self.base_total = 0
	#VERSION 1
	#here we are assuming everyone belongs to this event
	def findBest(persons, events):
		total = 0
		for e in events:
			weight = e.WEIGHT
			length = e.LENGTH
			[day, slot, value] = locate(person, weight, length)
			total = total + value
			place(persons, weight, loc_day, loc_slot, length)


	#returns an index for where this event fits best
	def locate(persons, weight, length=1):	
		max_day = 0
		max_slot = 0
		max_sum = 0
		#FOR EACH DAY in the SCHEDULE
		for d in range(self.utl.DAY):
			#FOR EACH TIME SLOT IN A DAY
			for t in range(self.utl.SLOT - length + 1):

				#EACH PERSON
				for p in persons:
					if w > p.SCHEDULE[d][t]
						day_slot_sum = day_slot_sum + w-p.SCHEDULE[d][t]

				#after each person is evaluation we check if this day/time was the best
				if day_slot_sum > max_sum:
					max_sum = day_slot_sum
					max_day = d
					max_slot = t

		return [max_day, max_slot, max_sum]

	def place(persons, weight, loc_day, loc_slot, length=1):
		for p in persons:
			for i in range(length): #0 to length-1
				if weight > p.SCHEDULE[loc_day][loc_slot+i]: 
					p.SCHEDULE[loc_day][loc_slot+i] = weight


	def valueOf(persons):
		val = 0
		for p in persons:
			for d in range(self.utl.DAY):
				for t in range(self.utl.SLOT)
					val += p.SCHEDULE[d][t]

		return val
# def comb(S, i, k, L):
# 	if S[i] == (k-L+1):
# 		return

# 	for j in range(S[i-1],k):


# 1 2 3
# 1 2 4
# 1 2 5
# 1 3 4
# 1 3 5
# 1 4 5
# 2 3 4
# 2 3 5
# 2 4 5
# 3 4 5