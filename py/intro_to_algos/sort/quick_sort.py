from ds import arrays
import sys
import random
import selection_sort
from profile import profile
@profile
def sort(a):
    quick_sort(a, 0, len(a)-1)

def quick_sort(a, start_index, end_index):
    if(start_index >= end_index):
        return 
    length = end_index - start_index + 1
    if(length<20):
        selection_sort.selection_sort(a,start_index,length)
        return
    randomize_input(a, start_index, end_index)
    split = partition(a, start_index, end_index)
    quick_sort(a, start_index, split - 1)
    quick_sort(a, split + 1, end_index) 
 
def randomize_input(a, start_index, end_index):
    rand = random.randint(start_index, end_index)
    a[end_index], a[rand] = a[rand], a[end_index]

def partition(a, start, end):
    pivot = a[end]
    i, j = start,end
    while(i<j):
        while(a[i]<pivot and i<j):
            i += 1
        while(a[j] >= pivot and j>i):
            j -= 1

        if(i<j):
            a[i], a[j] = a[j], a[i]
            
    a[j], a[end]= pivot, a[j]
    return j

def main():
    a = arrays.make(sys.argv)
    sys.setrecursionlimit(2**31-1)
    sort(a)
    return a

if __name__=="__main__":
     main()
#for (( i=0 ;i<3 ;i++ )) time python quick_sort.py 1000000 true
