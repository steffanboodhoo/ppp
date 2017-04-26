import timeit

def exam(n=10):
	v = 0
	print n
	# print '\nv is :',v

# def main():
def mod(x):
	# print x
	x['a'] = 'exam'


def foo():
	i = None
	for i in range (10):
		print (timeit.timeit("exam(i);", number=1, setup="from foo import i, exam"))

if __name__ == '__main__':
	foo()
	# print 'fuck my life'

	exam()
	x = 100
	setup = '''from __main__ import exam, mod,x,n; y = 20; z = 30 '''
	n = {}

	print (timeit.timeit("mod(n)", number=1, setup=setup))
	print n
	# print __main__
	# print x
	# print (timeit.timeit("exam(y)", number=20, setup=setup))
	# print (timeit.timeit("exam(z)", number=20, setup=setup))
	
	
	# exam(30)