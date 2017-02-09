from PatternSingleton import Singleton

@Singleton
class Utils:

	# _instance = None

	# @staticmethod
	# def getInstance(x):
	# 	if Utils._instance is None: 
	# 		Utils._instance = Utils()
	# 		print '~~~ created instance'
	# 	else:
	# 		print '~~~ instance already created'
	# 	return Utils._instance

	def __init__(self):
		print 'Utils created'
		#number of clusters
		self.K_CLUSTERS = 16

		# SCHEDULE
		self.DAY = 5
		self.SLOT = 18

		# PERSONAL
		self.VAL = 3
		self.PERSONAL_E_MAX = 5
		self.PERSONAL_E_MIN = 2

		# DEPARTMENTS - PERSONS
		self.DEPT_COUNT = 4 #number of departments
		self.PER_DEPT = 50

		# DEPARTMENT-EVENTS
		# TYPE A - PER DEPARTMENT
		self.DEPT_EVENTS_A = 1000
		self.A_INVITE_MAX = 10
		self.A_INVITE_MIN = 3

		# TYPE B - INTER DEPT MEETING
		self.DEPT_EVENTS_B = 4
		self.B_INVITE_MAX = 4
		self.B_INVITE_MIN = 2

		self.GLOBAL_MEETINGS = 2
