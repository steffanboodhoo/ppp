from Clus import core
import copy
from Scheduling import EventManipulation as evman
from Generate import gen
from Config import Utils
from Scheduling import group
import time

def main():
	utl = Utils.Instance()
	#Generate People P (their personal schedules), and place them into departments depts 
	[P,depts] = gen.genP()
	#create a copy of everyone's raw schedules base_P
	base_P = copy.deepcopy(P) 
	#generate events E, for persons in each department
	E = gen.genE(utl, P, depts)

	#create a set of empty clusters C, with centroids being a person from a department
	C = core.initClusters(P, utl.K, depts)
	#place the persons in these clusters
	C = core.placePeople(P,C)


	for c in C:
		start = time.time()
		c.scheduleClusterP1( copy.deepcopy(E), copy.deepcopy(P) )
		end = time.time()
		print end - start

	print evman.totalSum(P=P,utl=utl)

	group.evaluateClusterPlacements(E, P, C)
	for e in E:
		evman.placeEvent(e, P)

	print evman.totalSum(P=P,utl=utl)


if __name__ == '__main__':
	main()