from Clus import core
import copy
from Scheduling import EventManipulation as evman

from Generate import gen, extend

from Config import Utils
from Scheduling import group
import time, timeit

def varyEvents():
	print '---------------------JUST STARTED---------------------'
	utl = Utils.Instance()
	#Generate People P (their personal schedules), and place them into departments depts 
	[base_P,depts] = gen.genP()
	#generate events E, for persons in each department
	print '---------------print before events'
	print utl
	base_E = gen.genE(utl, base_P, depts)
	print '----------------- ABOUT TO LOOP'

	iterations=10
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

		temp_E = copy.deepcopy(base_E)
		temp_P = copy.deepcopy(base_P)
		#create a set of empty clusters C, with centroids being a person from a department
		C = core.initClusters(temp_P, utl.K_CLUSTERS, depts)
		#place the persons in these clusters
		C = core.placePeople(base_P, C)
		
		max_sched = 0
		#for each cluster
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

		print 'unclustered time',unclustered_time
		print 'clustered time',clustered_time
		val = ((unclustered_time - clustered_time)/clustered_time) * 100
		print '(total_clustered - unclustered)/clustered_time * 100:',val

		graph.append((len(base_E),val))
		extend.extendEvents(E=base_E, P=base_P, depts=depts, k=3200)
		
	print graph
	return graph

# def test():
# 	utl = Utils.Instance()
# 	#Generate People P (their personal schedules), and place them into departments depts 
# 	[base_P,depts] = gen.genP()
# 	#generate events E, for persons in each department
# 	base_E = gen.genE(utl, base_P, depts)

# 	print base_P
# 	print base_E

# def varyClusters():
# 	utl = Utils.Instance()
# 	#Generate People P (their personal schedules), and place them into departments depts 
# 	[base_P,depts] = gen.genP()
# 	#generate events E, for persons in each department
# 	base_E = gen.genE(utl, base_P, depts)

# 	iterations=3
# 	graph = []
# 	for i in range(iterations):
# 		temp_E = copy.deepcopy(base_E)
# 		temp_P = copy.deepcopy(base_P)
# 		#Unclustered TS
# 		start = time.time()
# 		evman.TS(temp_E, temp_P)
# 		evman.CA(temp_E, temp_P, base_P)
# 		end = time.time()
# 		unclustered_time = end - start

# 		temp_E = copy.deepcopy(base_E)
# 		temp_P = copy.deepcopy(base_P)

		
# 		utl.K_CLUSTERS = utl.K_CLUSTERS + 1
# 		# create a set of empty clusters C, with centroids being a person from a department
# 		C = core.initClusters(base_P, utl.K_CLUSTERS, depts)
# 		#place the persons in these clusters
# 		C = core.placePeople(base_P,C)

# 		max_sched = 0
# 		#for each cluster
# 		for c in C:
# 			ctemp_E = copy.deepcopy(temp_E)
# 			ctemp_P = copy.deepcopy(temp_P)
# 			print 'length of base_E',len(temp_E)
# 			print 'length of clusters - ', len(c.members)
# 			start = time.time()
# 			c.scheduleClusterP1( ctemp_E, ctemp_P, base_P )
# 			end = time.time()
# 			max_sched = max(end - start, max_sched)	


# 		#evaluate the placements for events across all clusters (choose the best|only placement for an event across clusters)
# 		start = time.time()
# 		group.evaluateClusterPlacements(temp_E, temp_P, C)
# 		for e in temp_E:
# 			evman.placeEvent(e, temp_P)
# 		end = time.time()
# 		clustered_time = (end - start) + max_sched

# 		# print 'unclustered time',unclustered_time
# 		# print 'clustered time',clustered_time
# 		val = ((unclustered_time - clustered_time)/clustered_time) * 100
# 		# print '(total_clustered - unclustered)/clustered_time * 100:',val

# 		graph.append((len(base_E),val))

# 	print '==============',utl.DEPT_EVENTS_A
# 	print graphs
# 	print '----------------)*#^$R(&#$GR'
# 	return graphs

#values is a vector of vectors
#each sub vector contains data points representing a graph
# subvector example [ (x1,y1), (x2,y2), (x3,y3) ]
# we want to find the average yi given an xi

def avg_values( values):
	avg_values= []

	for j in range(len(values[0])):
		val = 0
		for graph in values:
			val = val + graph[j][1]

		val = val / (len(values)*1.0)
		avg_values.append((values[0][j][0], val))

	return avg_values

if __name__ == '__main__':
	utl = Utils.Instance()
	run_amount = 2
	utl.K_CLUSTERS = 2
	values = []
	print 'fuck'
	# print 
	base_events = utl.DEPT_EVENTS_A
	for i in range(10):
		utl.DEPT_EVENTS_A = base_events
		graph = varyEvents()
		print graph
		values.append(graph)
	print 'finished simulations'
	graph = avg_values(values)
	print graph
	# for i in range(run_amount):
		# values.append(varyEvents())
	# test()