from Clus import core
import copy
from Scheduling import EventManipulation as evman

from Generate import gen, extend

from Config import Utils
from Scheduling import group
import time, timeit
from pprint import pprint

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
	clusters_count = [2**c for c in range(1,5)]
	iterations=3
	time_graph = []
	weight_graph = []

	for i in range(iterations):
		sub_graph_time = []	
		sub_graph_weight = []
		#UNCLUSTERED
		temp_E = copy.deepcopy(base_E)
		temp_P = copy.deepcopy(base_P)
		#Unclustered TS
		start = time.time()
		evman.TS(temp_E, temp_P)
		evman.CA(temp_E, temp_P, base_P)
		end = time.time()
		unclustered_time = end - start
		sub_graph_time.append((1,unclustered_time))
		sub_graph_weight.append((1, evman.totalSum(temp_P)))
		#VARIED CLUSTERS
		for curr_clusters_amount in clusters_count:
			#SET NUMBER OF CLUSTERS TO RUN WITH
			utl.K_CLUSTERS = curr_clusters_amount

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
				print 'Cluster Members - ', len(c.members)
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
			sub_graph_time.append((curr_clusters_amount, clustered_time))
			sub_graph_weight.append((curr_clusters_amount, evman.totalSum(temp_P)))
			# print 'unclustered time',unclustered_time
			# print 'clustered time',clustered_time
			# val = ((unclustered_time - clustered_time)/clustered_time) * 100
			# print '(total_clustered - unclustered)/clustered_time * 100:',val

		time_graph.append((len(base_E),sub_graph_time))
		weight_graph.append((len(base_E),sub_graph_weight))
		extend.extendEvents(E=base_E, P=base_P, depts=depts, k=5000)
		
	print weight_graph
	return time_graph

def convert( graph ):
	n_graph = {}
	for point_values in graph: #  (x, [ (f1,f1(x)), (f2, f2(x)), (f3,f3(x)) ])
		point = point_values[0] # x
		values = point_values[1] # [ (f1,f1(x)), (f2, f2(x)), (f3,f3(x)) ]
		for v in values:
			if not (v[0] in n_graph):
				n_graph[v[0]] = []
			n_graph[v[0]].append(v[1])
	print n_graph

def avg_values( values):
	avg_values= []

	for j in range(len(values[0])):
		val = 0
		for graph in values:
			val = val + graph[j][1]

		val = val / (len(values)*1.0)
		avg_values.append((values[0][j][0], val))

	return avg_values

	def avg_vals():
		for x in x_vals:
			for c in c_vals:
				for graph in values:

if __name__ == '__main__':
	utl = Utils.Instance()
	run_amount = 2
	utl.K_CLUSTERS = 2
	values = []
	base_events = utl.DEPT_EVENTS_A
	for i in range(10):
		utl.DEPT_EVENTS_A = base_events
		graph = varyEvents()
		print convert(graph)
		values.append(graph)

	pprint(values)
	# return 0 
	'''
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
	'''