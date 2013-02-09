from ds import arrays
from profile import profile
import sys

@profile
def sort(arr):
    counts = [0] * (len(arr) + 1)
    for ele in arr:
        if ele > len(arr):
            raise Exception("Cannot sort array: %s is greater than input array size %s" %
                            (ele, len(arr)))
        counts[ele] += 1
    count = 0
    for i, ele in enumerate(counts):
        count += counts[i]
        counts[i] = count
    sorted_arr = [0] * len(arr)
    for ele in reversed(arr):
        idx = counts[ele] - 1
        assert idx < len(sorted_arr)
        sorted_arr[idx] = ele
        counts[ele] -= 1
    arr[:] = sorted_arr
        
def main():
    a = arrays.make(sys.argv)
    sort(a)
    return a

if __name__=="__main__":
    main()
        
