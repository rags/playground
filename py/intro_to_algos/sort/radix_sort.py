from ds import arrays
from profile import profile
import sys
import math
import counting_sort

def digit(i, base):
    def extract(ele):
        return ele // base ** i % base
    return extract
        
@profile
def sort(arr, base=16):
    if not arr:
        return arr
    max_ele = max(arr)
    if not max_ele:
        return arr
    num_digits = int(math.ceil(math.log(max_ele, base)))
    a = arr
    for i in range(0, num_digits + 1):
        a = rearrange(a, i, base)
    arr[:] = a
        
def rearrange(arr, digit, base):
    counts = [0] * (base + 1)
    for ele in arr:
        counts[ele // base ** digit % base] += 1
    
    count = 0
    for i, ele in enumerate(counts):
        count += counts[i]
        counts[i] = count
        
    sorted_arr = [None] * len(arr)

    for ele in reversed(arr):
        i = ele // base ** digit % base
        idx = counts[i] - 1
        sorted_arr[idx] = ele
        counts[i] -= 1
    return sorted_arr
    
@profile
def sort_alphanum(arr):
    pass


        
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

        
