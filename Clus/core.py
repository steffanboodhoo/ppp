from random import randint, sample

import distance as distfn
from Models.Cluster import Cluster
# def cluster():
# //input: K, set of points x1...xn
# //place centroids c1...ck at random locations

# //repeat until convergence or something else:
# //for each point xi
# 	//find the nearest centroid
# 	//assign the point x to cluster j 
# //for each cluster j=1 to k
# 	//new centroid cj = mean of all points x1 assigned to cluster j in previous step

#this INF must be bigger than the one used in jaccard index
INF = 99999999999

def initClusters(P, k, depts):
	locations = [] #keeps track of which persons we selected so we won't initialize 2 of the same
	C = [] 
	for i in range(k):
		j = i%len(depts)
		p_i = sample(depts[j], 1)[0]

	 	while p_i in locations:
	 		p_i = sample(depts[j], 1)[0]

	 	locations.append(p_i)
	 	C.append( Cluster(id=i, centroid=P[p_i].events))

	return C

def placePeople(P, C):
	for p_i in range(len(P)):
		c_i = findCluster(P[p_i], C)
		C[c_i].members.append(p_i)
	return C

def findCluster(person, C):
	min_dist = INF
	min_ci = None

	for c_i in range(len(C)):
		dist = distfn.jaccardIndex( person.events, C[c_i].centroid )
		# dist = distfn.compareDiff( person.events, C[c_i].centroid )
		if dist < min_dist:
			min_dist = dist
			min_ci = c_i
	return min_ci


if __name__ == '__main__':
	print 'hello world'






