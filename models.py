from pprint import pprint
import random



class Person(object):
	def __init__(self,utils, id, dept):
		self.id = id
		self.events = []
		self.dept = dept
		self.role = None
		self.SCHEDULE = None
		self.fillSchedule(utils)
		self.cluster = None

	def fillSchedule(self, utl):
		self.SCHEDULE = [[utl.VAL for i in range(utl.SLOT)] for i in range(utl.DAY)]

		# number of personal events
		personal_e_count = random.randint(utl.PERSONAL_E_MIN, utl.PERSONAL_E_MAX) 
		i = 0
		while i < personal_e_count:
			day = random.randint(0,utl.DAY-1)
			slot = random.randint(0,utl.SLOT-1)
			if self.SCHEDULE[day][slot] == utl.VAL:
				val = random.randint(utl.VAL+1,10)
				self.SCHEDULE[day][slot] = val
				i+=1

	def __str__(self):
		return	'\nEVENTS:' + str(self.events) \
			+ '\nCLUSTER:' + str(self.cluster) \
			+ '\nSCHEDULE:'+ str(self.SCHEDULE)



class Event(object):
	def __init__(self, id, weight, length=1):
		self.id = id
		self.day = None
		self.slot = None
		self.weight = weight
		self.length = length
		self.invited = []

	def inviteA(self, dept, utl, P):
		invite_count = random.randint( utl.A_INVITE_MIN, utl.A_INVITE_MAX)
		self.invited = random.sample(dept['P'], invite_count)

		for p_i in self.invited:
			P[p_i].events.append(self.id)

	def __str__(self):
		return 'ID:' + str(self.id) \
			+'\nDAY:'+ str(self.day) + '   SLOT:' + str(self.slot) \
			+'\nINVITED:'+str(self.invited)

# class 
if __name__ == '__main__':
	p = Person()