import matrix
import sys
import timeit
#O(n**phi)
def fibonacci_recur(n):
 	if(n<1):
		return 0
	if(n<=2):
		return 1
	return fibonacci_recur(n-1) + fibonacci_recur(n-2)
#O(n)
def fibonacci_iter(n):
	if(n<1):
		return 0	
	a,b=1,1
	for i in xrange(2,n):
	    next = a + b
	    a = b
	    b = next
	return b
# _         _
# |Fn+1  Fn |
# |Fn   Fn-1|
#
MATRIX_FORM = [[1,1],
	       [1,0]] 
#O(logn)
def fibonacci_matrix(n):
	nth_matrix = matrix.exp(MATRIX_FORM,n)
	return nth_matrix[0][1]

def main():
	if(len(sys.argv)<3):
		print "usage: python %s n i #n = nth fib, i = 0,1,2 for matrix, iter, recur" % sys.argv[0]
		sys.exit()
	n = int(sys.argv[1])
	i = int(sys.argv[2])
	map = [("times for matrix form: ",fibonacci_matrix),
	       ("times for iterative method: ", fibonacci_iter), 
	       ("times for recursion: ", fibonacci_recur)]
	print map[i][0], map[i][1](n)


	# print "times for matrix form: ", timeit.Timer(lambda : fibonacci_matrix(n)).timeit()
	# print "times for iterative method: ", timeit.Timer(lambda: fibonacci_iter(n)).timeit()
	# print "times for recursion: ", timeit.Timer(lambda: fibonacci_recur(n)).timeit()

if __name__=="__main__":
	main()
########################################tests########################################
def assert_fib(n,result):
	assert fibonacci_matrix(n)==result
	assert fibonacci_iter(n)==result
	assert fibonacci_recur(n)==result
	
def should_calculate_nth_fib():
	assert_fib(3,2)
	assert_fib(5,5)
	assert_fib(19,4181)

