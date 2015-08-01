#compress aaaabbaaaa -> 4a2b4a
def compress(str):
    last_char=None
    cnt=0
    for c in str:
        if c==last_char:
            cnt +=  1
        else:
            if last_char:
                yield "%s%s" % (cnt,c)
            last_char=c
        
    if last_char:
        yield ("%s%s" % (cnt,c))


'''
Complexity Analysis -

Intuition of algorithm:
naive algorithm is O(N). O(logN) can be acheived using binary search if the size is known.
For unknown sized array the intuition of binary search can be used.
The basic approach expands the search scope by doubling the scope
(as apposed to b-search approach of cutting scope down by 1/2).
So the approach is inspired by binary search and tries to acheive similar runtime

Formal analysis:
partition is a recursive procedure. The size of the array decreases by 1/2 for each recursive call.
At each level of recursion there log N iterations
where N is number of 1's in top level call
then N/2 in 1st recursive call and N/4 in 2nd  recursive calland so on

So
T(N) = log2(N) + log2(N/2) + log2(N/4) + .... log(16) + log(8) + log(4) + log(2) + log(1) 

     *****WRONG ANALYSIS*****
     dropping the lower order terms we get
     
      ----------------
     | T(N) = O(logN) | - This was my earlier hand waving kind of analysis
      ----------------
     
*****CORRECT ONE******

T(N) = log2(N) + log2(N/2) + log(N/4) ..... + 4 + 3 + 2 + 1 + 0
       this is sum of series [formula: m(m+1)/2]
     = log(N) * (log(N)+1)/2
     = (log(N)^2)/2+ log(N)/2

Now dropping the lower order terms and constants we get

 ----------------
| T(N) = O(log^2N) | - Order log-square-N
 ----------------

'''
    
#partition array of 1's followed by zeros. unknown length. So cant use len()
#return index of first ocuurance of 0

def partition(a, i=0):
    if not a:
        return -1
    if a[i] == 0:
        return i
    try:
        if a[i + 1] == 0:
            return i + 1
    except IndexError:
        return -1 #all ones
    pow2 = 1
    while True: #log(N)
        j = i + 2 ** pow2
        try:
            if a[j] == 0:
                return partition(a, i + 2 ** (pow2 - 1))
        except IndexError:
            return partition(a, i + 2 ** (pow2 - 1))
        pow2 += 1
    raise Exception("Should never get here")


# Order log(N)
def partition_better(a, i=0):
    if not a:
        return -1
    if a[i] == 0:
        return i
    try:
        if a[i + 1] == 0:
            return i + 1
    except IndexError:
        return -1 #all ones
    pow2 = 1
    while True: #log(N)
        j = i + 2 ** pow2
        try:
            if a[j] == 0:
                return binary_search(a, i, j)
        except IndexError:
            return partition(a, i + 2 ** (pow2 - 1))
        pow2 += 1
    raise Exception("Should never get here")

#Log(N)
def binary_search(a, low, high):
    if low + 1 >= high :
        return low if a[low] == 0 else high if a[high] == 0 else -1
    mid = (low + high) // 2
    if a[mid] == 0:
        return binary_search(a, low, mid)
    return binary_search(a, mid + 1, high)
    
############################## unit tests ##############################
import pytest
@pytest.mark.parametrize(("algorithm"), [partition, partition_better])
def should_parition(algorithm):
    assert -1 == algorithm([1, 1, 1])
    assert -1 == algorithm([1])
    assert -1 == algorithm([])
    assert 0 == algorithm([0])
    assert 1 == algorithm([1, 0])
    assert 7 == algorithm([1, 1, 1, 1, 1, 1, 1, 0])
    assert 7 == algorithm([1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
    assert 9 == algorithm([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    

import random
@pytest.mark.parametrize(("algorithm"), [partition, partition_better])
def should_partition_large(algorithm):
    large = 100000
    for i in range(100):
        index = random.randint(1, large) #random partition
        a = [1] * index + [0] * (large - index) #index no of 1's followed by zeros
        assert index == algorithm(a)
        assert 0 == a[index] 
        assert 1 == a[index - 1] 
    
        
    
    
    