from Clus import core
import copy
from Scheduling import EventManipulation as evman

from Generate import gen, extend

from Config import Utils
from Scheduling import group
import time, timeit
from pprint import pprint

def varyEvents():
	
	utl = Utils.Instance()
	
	#Generate People P (Personal Schedules), depts contain references to people for their dept 
	[base_P, depts] = gen.genP()

	#generate events E, for persons in each department
	base_E = gen.genE(utl, base_P, depts)
	return


	clusters_count = [2**c for c in range(1,5)] #[2^1, 2^2, 2^3, 2^4]
	iterations=2
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

		time_graph.append((len(base_E),sub_graph_time))
		weight_graph.append((len(base_E),sub_graph_weight))
		extend.extendEvents(E=base_E, P=base_P, depts=depts, k=30)
		
	# print weight_graph
	return [time_graph, weight_graph]

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




if __name__ == '__main__':
	varyEvents()
	import sys
	sys.exit()
	utl = Utils.Instance()
	run_amount = 2
	utl.K_CLUSTERS = 2
	weight_values = []
	time_values = []
	base_events = utl.DEPT_EVENTS_A
	for i in range(20):
		utl.DEPT_EVENTS_A = base_events
		graph = varyEvents()
		time_values.append(graph[0])
		weight_values.append(graph[1])


	records = len(weight_values)
	events = len(weight_values[0])
	clusters = len(weight_values[0][0][1])

	# pprint (weight_values[0][0])
	w_cluster_graphs = {}
	for cluster in range(clusters): # 1 2 4 8 16 32
		w_cluster_graphs[cluster] = []

		for event in range(events):
			sum = 0
			for record in range(records):		
				sum = sum + weight_values[record][event][1][cluster][1]
			w_cluster_graphs[cluster].append(sum/(records*1.0))

	t_cluster_graphs = {}
	for cluster in range(clusters): # 1 2 4 8 16 32
		t_cluster_graphs[cluster] = []

		for event in range(events):
			sum = 0
			for record in range(records):		
				sum = sum + time_values[record][event][1][cluster][1]
			t_cluster_graphs[cluster].append(sum/(records*1.0))


	x_values = []
	for event in range(events):
		x_values.append(weight_values[0][event][0])
	# print x_values


	import plotly.plotly as py
	import plotly.graph_objs as go
	import plotly.tools as tools

	tools.set_credentials_file(username='boodhoo100', api_key='AhDBNZz4OORUm26OMul6')
	data = []
	for i in w_cluster_graphs.keys():
		val = 2**i
		graph = go.Scatter(
			x = x_values,
			y = w_cluster_graphs[i],
			name = str(val)+' clusters w'
		)
		data.append(graph)
	py.plot(data, filename='weight')


	data = []
	for i in t_cluster_graphs.keys():
		val = 2**i
		graph = go.Scatter(
			x = x_values,
			y = t_cluster_graphs[i],
			name = str(val)+' clusters t'
		)
		data.append(graph)

	py.plot(data, filename='time')
