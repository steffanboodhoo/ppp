from Clus import core
import copy
from Scheduling import EventManipulation as evman

from Generate import gen, extend

from Config import Utils
from Scheduling import group
import time

def varyEvents():
	utl = Utils.Instance()
	#Generate People P (their personal schedules), and place them into departments depts 
	[base_P,depts] = gen.genP()
	#generate events E, for persons in each department
	base_E = gen.genE(utl, base_P, depts)
	
	
	for i in range(2):
		temp_E = copy.deepcopy(base_E)
		temp_P = copy.deepcopy(base_P)
		#Unclustered TS
		start = time.time()
		print 'start unclustered-',start
		evman.TS(temp_E, temp_P)
		evman.CA(temp_E, temp_P, base_P)
		end = time.time()
		print 'end unclustered-',end
		unclustered_time = end - start
		print 'unclustered time',unclustered_time


		temp_E = copy.deepcopy(base_E)
		temp_P = copy.deepcopy(base_P)
		#create a set of empty clusters C, with centroids being a person from a department
		C = core.initClusters(temp_P, utl.K_CLUSTERS, depts)
		#place the persons in these clusters
		C = core.placePeople(base_P, C)
		
		# for c in C:
		# 	print 'member count',len(c.members)
		# return
		max_sched = 0
		#for each cluster
		
		for c in C:
			ctemp_E = copy.deepcopy(temp_E)
			ctemp_P = copy.deepcopy(temp_P)
			print len(base_E),'before start----------------'
			start = time.time()
			print 'cluster sched start',start
			#schedule the events for that cluster
			c.scheduleClusterP1( ctemp_E, ctemp_P, base_P )
			end = time.time()
			print 'cluster sched end',end
			max_sched = max(end - start, max_sched)	
			print 'cluster time',max_sched


		#evaluate the placements for events across all clusters (choose the best|only placement for an event across clusters)
		start = time.time()
		group.evaluateClusterPlacements(temp_E, temp_P, C)
		for e in temp_E:
			evman.placeEvent(e, temp_P)
		end = time.time()
		clustered_time = end - start + max_sched

		print (max_sched - unclustered_time)

		extend.extendEvents(E=base_E, P=base_P, depts=depts, k=1000)
		print len(base_E),'after extension ----------------'

	# print evman.totalSum(P=P)

# def varyClusters():
# 	utl = Utils.Instance()
# 	#Generate People P (their personal schedules), and place them into departments depts 
# 	[base_P,depts] = gen.genP()
# 	#generate events E, for persons in each department
# 	base_E = gen.genE(utl, base_P, depts)

# 	for i in range(10):
# 		utl.K_CLUSTERS = utl.K_CLUSTERS + 1
# 		#create a set of empty clusters C, with centroids being a person from a department
# 		C = core.initClusters(base_P, utl.K_CLUSTERS, depts)
# 		#place the persons in these clusters
# 		C = core.placePeople(base_P,C)

if __name__ == '__main__':
	varyEvents()