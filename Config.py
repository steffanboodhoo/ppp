from PatternSingleton import Singleton

@Singleton
class Utils:
	
	def __init__(self):
		#number of clusters
		self.K_CLUSTERS = 3

		# SCHEDULE
		self.DAY = 5
		self.SLOT = 18

		# PERSONAL
		self.PERSONAL_VALUE_BOUND = 3
		self.PERSONAL_E_MAX = 5
		self.PERSONAL_E_MIN = 2

		# DEPARTMENTS - PERSONS
		self.DEPT_COUNT = 2 #number of departments
		self.PER_DEPT = 50

		# DEPARTMENT-EVENTS
		# TYPE A - PER DEPARTMENT
		self.DEPT_EVENTS_A = 500
		self.A_INVITE_MAX = 5
		self.A_INVITE_MIN = 3

		# TYPE B - INTER DEPT MEETING
		self.DEPT_EVENTS_B = 4
		self.B_INVITE_MAX = 5
		self.B_INVITE_MIN = 2

		self.GLOBAL_MEETINGS = 2
