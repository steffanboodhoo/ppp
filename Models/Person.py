from Config import Utils
import random

utl = Utils.Instance()
class Person(object):

	def __init__(self, id, dept):

		self.id = id
		self.events = []
		self.dept = dept
		self.role = None
		self.SCHEDULE = None
		self.fillSchedule()
		self.cluster = None

	def fillSchedule(self):
		self.SCHEDULE = [[utl.PERSONAL_VALUE_BOUND for i in range(utl.SLOT)] for i in range(utl.DAY)]

		# number of personal events
		personal_e_count = random.randint(utl.PERSONAL_E_MIN, utl.PERSONAL_E_MAX) 
		i = 0
		while i < personal_e_count:
			day = random.randint(0,utl.DAY-1)
			slot = random.randint(0,utl.SLOT-1)
			if self.SCHEDULE[day][slot] == utl.PERSONAL_VALUE_BOUND:
				val = random.randint(utl.PERSONAL_VALUE_BOUND+1,10)
				self.SCHEDULE[day][slot] = val
				i+=1

	def __str__(self):
		return	'\nEVENTS:' + str(self.events) \
			+ '\nCLUSTER:' + str(self.cluster) \
			+ '\nSCHEDULE:'+ str(self.SCHEDULE)