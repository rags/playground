from ds import arrays
import sys
import numpy.random as rand
from profile import profile
@profile
def sort(a):
    a[:] = _sort(a)
    
def _sort(a):
    if len(a) < 2:
        return a
    rand_idx = rand.randint(0, len(a))
    return _sort([i for i in a if i <= a[rand_idx]]) + _sort([i for i in a if i > a[rand_idx]])

def main():
    a = arrays.make(sys.argv)
    sys.setrecursionlimit(2**31-1)
    sort(a)
    return a

if __name__=="__main__":
    main()
#for (( i=0 ;i<3 ;i++ )) time python quick_sort.py 1000000 true
