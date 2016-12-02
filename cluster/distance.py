def main():
	print 'hello'
	print 'larger is further :'+ str( m,( [1], [2,3,4] ))
	print 'larger is closer :'+ str(compareSame( [1], [2,3,4] ))

#THE INVERSE IS BETTER
def compareDiff(X,Y):
	x_length = len(X)
	y_length = len(Y)

	diff = i = j = 0
	while(i!=x_length and j!=y_length):
		if X[i]==Y[j]:
			i+=1
			j+=1
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


if __name__ == '__main__':
	main()