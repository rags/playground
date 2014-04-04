"""
Challenge 1: Deviation

Given an array of integer elements and an integer d please consider all the sequences of d consecutive elements in the array. For each sequence we compute the difference between the maximum and the minimum value of the elements in that sequence and name it the deviation.

Your task is to

    write a function that computes the maximum value among the deviations of all the sequences considered above
    print the value the standard output (stdout)

Note that your function will receive the following arguments:

    v
        which is the array of integers
    d
        which is an integer value giving the length of the sequences

Data constraints

    the array will contain up to 100,000 elements
    all the elements in the array are integer numbers in the following range: [1, 231 -1]
    the value of d will not exceed the length of the given array

Efficiency constraints

    your function is expected to print the result in less than 2 seconds

Example
Input 	Output

v: 6, 9, 4, 7, 4, 1
d: 3
	

6

Explanation

The sequences of length 3 are:

    6 9 4 having the median 5 (the minimum value in the sequence is 4 and the maximum is 9)
    9 4 7 having the median 5 (the minimum value in the sequence is 4 and the maximum is 9)
    7 4 1 having the median 6 (the minimum value in the sequence is 1 and the maximum is 7)
    The maximum value among all medians is 6

"""

def find_deviation(v, d):
   diff=None
   mn,mx=None,None
   for i in range(len(v)-d + 1):
       if diff is None:
           mn=min(v[i:i+d])
           mx=max(v[i:i+d])
           diff = mx - mn
           continue
       if mx != v[i - 1] and mn != v[i - 1] and mx > v[i + d - 1] and  mn < v[i + d - 1]:
           continue
       mn=min(v[i:i+d])
       mx=max(v[i:i+d])
           
       cur_diff=mx-mn
       if diff is None or cur_diff>diff:
            diff=cur_diff
   print diff
   return diff 

############################## TEST ##############################

import random

def should_find_max_diff():
    for i in range(10):
        a = range(25)
        random.shuffle(a)
        print a
        print [(max(a[i: i + 3]), min(a[i: i + 3])) for i in range(25 - 3)]
        assert  find_deviation(a, 3) == \
        max(max(a[i: i + 3]) - min(a[i: i + 3]) for i in range(25))
            
        
    