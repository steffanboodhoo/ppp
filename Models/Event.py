from Config import Utils
import random

utl = Utils.Instance()
class Event(object):
	def __init__(self, id, weight, length=1):
		self.id = id
		self.day = None
		self.slot = None
		self.weight = weight
		self.length = length
		self.invited = []

	def inviteA(self, P, dept):
		invite_count = random.randint( utl.A_INVITE_MIN, utl.A_INVITE_MAX)
		#invite 'invite_count' number of people
		self.invited = random.sample(dept, invite_count)
		
		#for each person invited, append event to their list of events 
		for p_i in self.invited:
			P[p_i].events.append(self.id)

	def __str__(self):
		return 'ID:' + str(self.id) \
			+'\nDAY:'+ str(self.day) + '   SLOT:' + str(self.slot) \
			+'\nINVITED:'+str(self.invited)
