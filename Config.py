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
		self.K = 3

		# SCHEDULE
		self.DAY = 2
		self.SLOT = 5

		# PERSONAL
		self.VAL = 3
		self.PERSONAL_E_MAX = 8
		self.PERSONAL_E_MIN = 5

		# DEPARTMENTS - PERSONS
		self.DEPT_COUNT = 3
		self.PER_DEPT = 3

		# DEPARTMENT-EVENTS
		# TYPE A - PER DEPARTMENT
		self.DEPT_EVENTS_A = 3
		self.A_INVITE_MAX = 3
		self.A_INVITE_MIN = 2

		# TYPE B - INTER DEPT MEETING
		self.DEPT_EVENTS_B = 4
		self.B_INVITE_MAX = 4
		self.B_INVITE_MIN = 2

		self.GLOBAL_MEETINGS = 2
