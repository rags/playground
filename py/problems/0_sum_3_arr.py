#find elements a,b,c in arr1,arr2,arr3 such that a+b+c=0
#naive solution O(n^3).
#next best O(nlog(n^2))

import numpy
import matrix_search

#n^2 solution
def zero_sum_nsq(arr1, arr2, arr3):
    assert len(arr1) == len(arr2) == len(arr3)
    arr1.sort() #nlogn
    arr2.sort()#nlogn
    matrix = numpy.add(numpy.transpose([arr1] * len(arr1)),
                       [arr2] * len(arr2)).tolist() #O(n^2)
    for e in arr3:
        loc = matrix_search.search(matrix,-e)
        if loc:
            return arr1[loc[0]], arr2[loc[1]], e

#This is nlogn solution
def zero_sum(arr1, arr2, arr3):
    assert len(arr1) == len(arr2) == len(arr3)
    arr1.sort() #nlogn
    arr2.sort(reverse=True)#nlogn

    #nlog(n)   [ i.e, n*log(n)]
    for e in arr3: #O(n)
        match =  search(arr1, arr2, (0, 0), (len(arr1), len(arr1)), e) #O(log(n))
        if match:
            return match
            
def search(arr1, arr2, (i, j), (m, n), ele):
    if not(i < m and j < n):
        return
    col_idx = (j + n) / 2
    to_search = -(ele + arr2[col_idx])
    row_idx = bs(arr1, i, m, to_search) #O(log(n))
    print row_idx, col_idx
    a1a2 = -(arr1[row_idx] + arr2[col_idx])
    if ele == a1a2:
        return (arr1[row_idx], arr2[col_idx], ele)

    if ele < a1a2:
        return (search(arr1, arr2, (i, j), (row_idx, col_idx), ele)
                or
                search(arr1, arr2, (i, col_idx), (row_idx, n), ele)
                or
                search(arr1, arr2, (row_idx, j), (m, col_idx), ele))
        
    return (search(arr1, arr2, (row_idx + 1, col_idx + 1), (m, n), ele)
            or
            search(arr1, arr2, (row_idx + 1, j), (m, col_idx + 1), ele)
            or
            search(arr1, arr2, (i, col_idx + 1), (row_idx + 1, n), ele))

    '''
    complexity of search method
    log(n) + 3T(1/4)
    = log(n) + 3(log(n/4)+ 3(T(1/16)))
    = log(n) + 3(log(n/4)+ 3(T(1/16)))
    = log(n) + 3(log(n/4)+ 3(log(1/16) + 3(T(1/64))))
    = log(n) + 3log(n/4)+ 9log(1/16) + 27T(1/64) + 81T(1/256) + .....
    = O(log(n))
    '''        
        
def bs(arr,  start, end, ele):
    assert start <= end - 1
    if start == end - 1:
        return start
    mid = (start + end) / 2
    if arr[mid] == ele:
        return mid
    if arr[mid] > ele:
        return bs(arr, start, mid, ele)
    if mid + 1 == end:
        return mid
    return bs(arr, mid + 1, end, ele)

#################### TESTS ####################
import pytest

@pytest.mark.parametrize(('algorithm'), [zero_sum, zero_sum_nsq])
def should_find_0_sum(algorithm):
    assert (-1,-1, 2) == algorithm([1, -1, 5], [ -1, 10, 13], [2,-2, 3])
    assert_res(algorithm, ([-5, 9, -1, 4, 7, -2], [-7, 6, 1, 5, -4, 8], [-15, -10, -7, 6, 9, 7]))
    (-5,-5, 10) == algorithm([-5, 10, 2, 3, 4], [ -5, -10, 6, 7, 8], [100, 200, 300, 10, 50])
    assert not algorithm([1, 3, 2], [4, 5, 6], [-20, -30, -10])


def assert_res(algorithm, arrs):
    res = algorithm(*arrs)
    for i, e in enumerate(res):
        assert e in arrs[i]
    assert 0 == sum(res)

#doc
 
'''
arr1=[-5,-2,-1,4,7,9] - sorted
arr2=[-7,-4, 1, 5, 6, 8] - sorted
arr3=[-15,-10,-7,6,7,9]

matrix of arr1+arr2

values increase from left to right and 

    [ -5,  -2,  -1,   4,   7,   9]
    ------------------------------
-7  [-12,  -9,  -8,  -3,   0,   2]
-4  [ -9,  -6,  -5,   0,   3,   5]
 1  [ -4,  -1,   0,   5,   8,  10]
 5  [  0,   3,   4,   9,  12,  14]
 6  [  1,   4,   5,  10,  13,  15]
 8  [  3,   6,   7,  12,  15,  17]

values increase from left to right and top to bottom

iterate through arr3 and binary search the matrix[i,j] such that arr3[k]+matrix[i,j]=0
'''    