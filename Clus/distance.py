INF = 9999999999
def main():
	print 'hello'
	print 'larger is further :'+ str( m,( [1], [2,3,4] ))
	print 'larger is closer :'+ str(compareSame( [1], [2,3,4] ))

#THE INVERSE IS BETTER
def compareDiff(X,Y):
	x_length = len(X)
	y_length = len(Y)

	diff = i = j = 0
	#i isn't at the end of X and j isnt at the end of Y
	while(i!=x_length and j!=y_length):
		#elements match so move forward
		if X[i]==Y[j]:
			i+=1
			j+=1
		#elements dont match, if Xi is bigger move Yj onto the next and add 1 to different elem count
		elif X[i]>Y[j]:
			j+=1
			diff+=1
		else:
			i+=1
			diff+=1

	remaining_elements = x_length - i + y_length - j
	diff += remaining_elements
	return diff

def compareSame(X,Y):
	x_length = len(X)
	y_length = len(Y)

	same = i = j = 0
	while(i!=x_length and j!=y_length):
		if X[i]==Y[i]:
			i+=1
			j+=1
			diff+=1

		elif X[i]>Y[j]:
			j+=1
		else:
			i+=1

	return same

# in jaccard Index closer to 1 means closer to being the same.
# we are going to return the inverse to keep it more standard therefore
# the closer to 1 the smaller number it would return meaning less distance 
# the closer to 0 the higher the number returned meaning greater distance
def jaccardIndex(X,Y):
	sx = set(X)
	sy = set(Y)
	intersection = sx & sy
	union = sx | sy
	if len(union) == 0: #both cluster and person has no elements
		return 0
	val = len(intersection)*1.0 / len(union)*1.0
	if val == 0: #this means the intersection was 0 meaning no similar elements
		return INF
	return 1/val


if __name__ == '__main__':
	main()