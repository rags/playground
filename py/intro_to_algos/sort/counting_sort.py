from ds import arrays
from profile import profile
import sys

#O(n+k) k is not size of max element
@profile
def sort(arr, key=None, no_of_slots = None):
    no_of_slots = no_of_slots or max(arr)
    counts = [0] * (no_of_slots + 1)

    if key:
        for ele in arr:
            counts[key(ele)] += 1
    else:
        for ele in arr:
            counts[ele] += 1
        
    
    count = 0
    for i, ele in enumerate(counts):
        count += counts[i]
        counts[i] = count
        
    sorted_arr = [None] * len(arr)
    if key:
        for ele in reversed(arr):
            i = key(ele)
            idx = counts[i] - 1
            sorted_arr[idx] = ele
            counts[i] -= 1
    else:
        for ele in reversed(arr):
            idx = counts[ele] - 1
            sorted_arr[idx] = ele
            counts[ele] -= 1
    print counts
    arr[:] = sorted_arr
        
def main():
    a = arrays.make(sys.argv)
    sort(a)
    return a

if __name__=="__main__":
    main()
#    a = range(10) + [5, 6, 9, 10]
#    print a
#    sort(a)
#    print a

        
