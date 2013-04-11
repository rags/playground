import sys
from ds import arrays
from profile import profile

#not an optiomal impl- just playing around

@profile
def sort(a, k=3):
    merge_sort(a,0,len(a),[0]*len(a), k)
    
def minp(a, parts):
    m = -1
    for i, p in enumerate(parts):
        if p[0] < p[1]:
            if m == -1 or a[p[0]] < a[parts[m][0]]:
                m = i
    return m
    
def merge_sort(a,start,end,result, k):
    ri = 0
    if end - start < k:
        if end - start > 1:
            #use heap sort (in place) to sort if partion can't be split'
            heapify(a, start, end)
            for i in range(start, end):
                delete(a, start, end - (i - start))
        return 
    else:
        part = (end - start) // k
        parts = []
        j = start
        for i in range(k - 1):
            merge_sort(a, j, j + part, result, k)
            parts.append((j, j + part))
            j += part
        merge_sort(a, j, end, result, k)
        parts.append((j, end))
        #print "parts:"
        #for p in parts:
        #    print a[p[0]: p[1]], p[0], p[1]
        while True:
            pi = minp(a, parts)
            if pi == -1:
                break
            result[ri] = a[parts[pi][0]]
            ri += 1
            parts[pi] = parts[pi][0] + 1, parts[pi][1]
            
    #print "Result: ", result[0 : ri]   
    i,j = start,0    
    while(j<ri):
        a[i], i, j = result[j], i+1, j+1


def left(i, start=0):
    return (i * 2 + 1) - start

def right(i, start=0):
    return (i * 2 + 2) - start
    
def max_i(a, i, start, end):
    m = i
    j, k = left(i, start), right(i, start)
    if j < end and a[j] > a[m]:
        m = j
    if k < end and a[k] > a[m] :
        m = k
    return m

def delete(a, start, end):
    if start == end - 1:
        return
    r = a[start]
    a[start], a[end - 1]= a[end - 1], a[start]
    sift_down(a, start, start, end - 1)
    return r
    
def heapify(a, start, end):
    for i in range(((start + end)// 2) - 1, start-1, -1):
        sift_down(a, i, start, end)
    return a
        
def sift_down(a, i, start, end):
    leaf_node = (start + end) // 2
    if i > leaf_node:
        return 
    j = max_i(a, i, start, end)
    if j!= i:
        a[i], a[j] = a[j], a[i]
        if j < leaf_node:
            sift_down(a, j, start, end)
        
def main():
    a = arrays.make(sys.argv)
    sys.setrecursionlimit(2**31-1)
    sort(a)
    return a

if __name__=="__main__":
    main()
else:
    
    from numpy import random as rand
    
    def should_sort():
        for i in [50, 100, 300, 1000, 10000, 100000]:
            a = range(i)
            rand.shuffle(a)
            sort(a)
            assert range(i) == a
            
    def should_heapify():
        assert heapify([1, 2, 3, 4], 0, 2) == [2, 1, 3, 4]
        assert heapify([1, 2, 3, 4], 2, 4) == [1, 2, 4, 3]
        assert heapify(range(10), 8, 10) == range(8) + [9, 8]
        assert [3, 2, 1] == heapify([3, 2, 1], 0, 3)
        for i in range(5):
            l = list(rand.randint(0, 100, size=25))
            heapify(l, 0, len(l))
            for i, e in enumerate(l):
                li, ri = left(i), right(i)
                if li < len(l):
                    assert e >= l[li]
                if ri < len(l):
                    assert e >= l[ri]