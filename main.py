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
	
	#GENERATE PERSONS base_P, ASSIGN TO DEPARTMENTS depts 
	[base_P, depts] = gen.genP()

	#GENERATE DEPARTMENT LEVEL EVENTS base_E
	base_E = gen.genE(utl, base_P, depts)

	#SIMULATION VARIABLES
	clusters_count = [2**c for c in range(1,4)] #[2^1, 2^2, 2^3] - different cluster amounts
	event_increment = 30	#the amount of events to add
	iterations = 2			#number of iterations - how many times we increase by event_increment
	
	#DATASTRUCTURES FOR RESULTS
	# results [ k clusters ] [iteration of k] - using k clusters, what is the value created for every K, K being set of event amounts
	cluster_times = [ [0]*iterations for i in range((len(clusters_count)+1)) ]  
	cluster_weights = [ [0]*iterations for i in range((len(clusters_count)+1)) ]

	#RUN THE SIMULATION 'iterations' TIMES 
	for i in range(iterations):
		
		#UNCLUSTERED 
		[ curr_time, curr_weight] = unclustered(base_E, base_P)
		cluster_times [0][i] = curr_time
		cluster_weights [0][i] = curr_weight

		#CLUSTERED
		for c in range(len(clusters_count)):
			#SET NUMBER OF CLUSTERS TO RUN WITH
			utl.K_CLUSTERS = clusters_count[c] # c is the index of the number of clusters
			[curr_time, curr_weight] = clustered(base_E, base_P, depts)
			cluster_times [c+1][i] = curr_time
			cluster_weights [c+1][i] = curr_weight		


		extend.extendEvents(E=base_E, P=base_P, depts=depts, k=event_increment)
		
	return [time_graph, weight_graph]

#Unclustered 
def unclustered(base_E, base_P):
	#COPY OF EVENTS AND PERSONS 
	temp_E, temp_P = copy.deepcopy(base_E), copy.deepcopy(base_P)
	
	start = time.time()				# start time
	evman.TS(temp_E, temp_P)		#Perform TS
	evman.CA(temp_E, temp_P, base_P)# Perform CA
	end = time.time()				# end time
	unclustered_time = end - start
	unclustered_weight = evman.totalSum(temp_P) #total weight
	return [unclustered_time, unclustered_weight]

def clustered(base_E, base_P, depts):
	utl = Utils.Instance()
	#COPY OF EVENTS AND PERSONS 
	temp_E, temp_P = copy.deepcopy(base_E), copy.deepcopy(base_P)

	#CREATE EMPTY CLUSTERS WITH CENTRIOD 
	C = core.initClusters(temp_P, utl.K_CLUSTERS, depts) # utl.K_CLUSTERS
	
	#TRAIN CLUSTERS
	#******TODO******

	#PLACE PERSONS IN CLUSTERS
	C = core.placePeople(base_P, C)

	max_sched = 0
	#FOR EACH CLUSTER
	for c in C:
		#CREATE A CLEAN COPY FOR EACH CLUSTER
		ctemp_E, ctemp_P = copy.deepcopy(temp_E), copy.deepcopy(temp_P)

		start = time.time()								#start time
		c.scheduleClusterP1( ctemp_E, ctemp_P, base_P )	#perform TS and CA
		end = time.time()								#end time
		#SAVE MAX TIME ACROSS ALL c IN C
		max_sched = max(end - start, max_sched)			


	start = time.time()
	#USE C {all clusters, now with events placed} TO CHOOSE BEST PLACEMENTS FOR E
	group.evaluateClusterPlacements(temp_E, temp_P, C)
	for e in temp_E:
		evman.placeEvent(e, temp_P)
	end = time.time()

	clustered_time = (end - start) + max_sched
	clustered_weight = evman.totalSum(temp_P)
	print clustered_time
	return [clustered_time, clustered_weight]

######################################################################################
################################ HELPER FUNCTIONS ####################################
######################################################################################
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
