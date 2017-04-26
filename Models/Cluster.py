from Config import Utils
from Scheduling import EventManipulation as evman, group

utl = Utils.Instance()

class Cluster(object):
	def __init__(self, id, centroid=None):
		self.id = id
		self.centroid = centroid
		self.members = []
		self.E = None
		self.Ec_d = None #Events of this Cluster, Distinct elements
		self.Ec_u = None #Events of this Cluster, Unique elements ( different from all other clusters)

	def recalculateCentroid(self, P, l):
		full_list = []
		for p_i in self.members:
			full_list.extend(P[p_i].events)

		#tallies the frequency of each number into counts
		counts = collections.Counter(full_list)
		#converts counts into a dict key - numebr, value = frequency
		count_dict = dict(counts)
		#converts dicts into a LIST of SORT tuples by value aka the frequency of that number, reverse is set so it can be descending
		freq_tuples = sorted(count_dict.items(), key=operator.itemgetter(1), reverse=True)
	

		#all numbers of the greaexam frequency will be stored in a list at aggr_freq[0] 
		#then all numbers of next greaexam frequency will be stored in a list at aggr_freq[1] and so on 
		aggr_freq = []
		freq = 0 #last common frequency

		for f_tuple in freq_tuples:
			#new frequency new list
			if f_tuple[1] != freq:
				freq = f_tuple[1]
				# aggr_freq[len(aggr_freq)] = []
				aggr_freq.append([f_tuple[0]])#add number as first item of new frequency list

			else:
				aggr_freq[len(aggr_freq)-1].append(f_tuple[0])
		
		
		k=0
		i=0
		j=0
		self.centroid = []
		while k<=l and i<len(aggr_freq):
			free = l - k + 1
			
			if len(aggr_freq[i])<=free:
				self.centroid.extend(aggr_freq[i])
				k += len(aggr_freq[i])
				i += 1
			else:
				r = random.sample(aggr_freq[i],free)
				self.centroid.extend(r)
				k += free

			

		

	def setDistinctEvents( self, P ):
		self.Ec_d = []
		print "number of members",len(self.members)
		for p_i in self.members:
			self.Ec_d.extend(P[p_i].events)
		self.Ec_d = set(self.Ec_d)


	def scheduleClusterP1(self, E, P, base_P):
		self.E = E
		self.setDistinctEvents(P)
		
		#Ec_linked contains a shallow copy of distinct events for this cluster 
		Ec_linked = group.getEventsSubsetShallow(E=E, indicies=list(self.Ec_d))

		evman.TS(E=Ec_linked, P=P)
		evman.CA(E=Ec_linked, P=P, base_P = base_P, full_E = E)

	def __str__(self):
		return '\nID' + str(self.id) + '\nCentroid:' + str(self.centroid) + '\nMembers:' + str(self.members)