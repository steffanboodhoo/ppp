from distance import compareDiff as dist_fn
from random import randint
# def cluster():
# //input: K, set of points x1...xn
# //place centroids c1...ck at random locations

# //repeat until convergence or something else:
# //for each point xi
# 	//find the nearest centroid
# 	//assign the point x to cluster j 
# //for each cluster j=1 to k
# 	//new centroid cj = mean of all points x1 assigned to cluster j in previous step


INF = 999999
def select_centroids(persons, k):
	locations = [] 
	centroids = [] 
	for i in range(k):
		l = randint(0,len(persons))
	 	while l in locations:
	 		l = randint(0,len(persons))
	 	locations.append(i)
	 	centroids.append(persons[i])
	return centroids

def place_points(persons, centroids):

	clusters = {}
	for p in persons:
		min_dist = INF
		min_clust = None

		#find cluster for this person
		for c in range(len(centroids)):# for each centroid
			dist = dist_fn( p.events, centroids[c])
			if dist < min_dist:
				min_dist = dist
				min_clust = c

		if  not min_clust in clusters:
			clusters[min_clust] = []
			
		clusters[min_clust].append(p) #adds person to cluster

	return clusters
			
def recalculate_centroids(clusters):
	
	for cluster in clusters:
		print

if __name__ == '__main__':
	print 'hello world'






