from Clus import core
import copy
from Scheduling import EventManipulation as evman

from Generate import gen, extend

from Config import Utils
from Scheduling import group
import time, timeit

def varyEvents():
	utl = Utils.Instance()
	#Generate People P (their personal schedules), and place them into departments depts 
	[base_P,depts] = gen.genP()
	#generate events E, for persons in each department
	base_E = gen.genE(utl, base_P, depts)
	
	iterations=5
	graph = []
	for i in range(iterations):
		temp_E = copy.deepcopy(base_E)
		temp_P = copy.deepcopy(base_P)
		#Unclustered TS
		start = time.time()
		evman.TS(temp_E, temp_P)
		evman.CA(temp_E, temp_P, base_P)
		end = time.time()
		unclustered_time = end - start
		# print 'unclustered time',unclustered_time


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
		c = None
		ctemp_E = None
		ctemp_P = None

		for c in C:
			ctemp_E = copy.deepcopy(temp_E)
			ctemp_P = copy.deepcopy(temp_P)
			print 'length of base_E',len(temp_E)
			print 'length of clusters - ', len(c.members)
			start = time.time()
			c.scheduleClusterP1( ctemp_E, ctemp_P, base_P )
			end = time.time()

			max_sched = max(end - start, max_sched)	


		#evaluate the placements for events across all clusters (choose the best|only placement for an event across clusters)
		start = time.time()
		group.evaluateClusterPlacements(temp_E, temp_P, C)
		for e in temp_E:
			evman.placeEvent(e, temp_P)
		end = time.time()
		clustered_time = (end - start) + max_sched

		# print (max_sched - unclustered_time)
		print 'unclustered time',unclustered_time
		print 'clustered time',clustered_time
		val = ((unclustered_time - clustered_time)/clustered_time) * 100
		print '(total_clustered - unclustered)/clustered_time * 100:',val

		graph.append((len(base_E),val))
		extend.extendEvents(E=base_E, P=base_P, depts=depts, k=3200)
		
	print graph
	# print evman.totalSum(P=P)

def test():
	utl = Utils.Instance()
	#Generate People P (their personal schedules), and place them into departments depts 
	[base_P,depts] = gen.genP()
	#generate events E, for persons in each department
	base_E = gen.genE(utl, base_P, depts)

	print base_P
	print base_E

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
	# test()