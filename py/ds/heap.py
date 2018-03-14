'''
A tree has n / 2 leaf nodes and n / 2 non leaf node.
to heapify start with the last parent node (n / 2) and work your way upto root (first element)
At each node find the max(parent,  left,  right) and swap it with parent.
If you swap with a non leaf child.   you will need to repeat the process with that child as parent

             0
            / \
           /   \
          1    2
         / \  / \
        3  4 5   6
       / \  \
      7  8  9
n = 10
leaf nodes =  5,  non leaf =  5
iteration begins at index 4 (n / 2 - 1) -> -1 beacause 0th based index
and ends at 0
left = i * 2 + 1
right = left + 1

'''
from __future__ import print_function
import math
from ds import arrays
import sys
        
def parent(i):
    assert i > 0
    return (i - 1) // 2
def left(i): return i * 2 + 1
def right(i): return i * 2 + 2

#def children(i, size=None):
#    l, r = left(i), right(i)
#    return (l, r) if not size else (i for i in (l, r) if i < size)

def children(i, size=None):
    l, r = left(i), right(i)
    if not size or r < size:
        return l, r
    if l < size:
        return l, 
    return tuple()   

class Heap(object):
    def __init__(self, vals=None,comparitor=cmp, fixed_size = False):
        self.vals = heapify(vals or [], comparitor) 
        self.cmp = comparitor
        self.fixed_size = fixed_size
        if fixed_size:
            assert vals, "should pass in arr with len()>0 for fixed size"
            self.max_size = len(vals)
            self.cur_size = len(vals)
        
    def __len__(self):
        return self.cur_size if self.fixed_size else len(self.vals)
        
    def pop(self):
        assert len(self) > 0
        last = len(self) - 1
        self.vals[0], self.vals[last] = self.vals[last], self.vals[0]
        if not self.fixed_size:
            val =  self.vals.pop()
        else:
            val = self.vals[last]
            self.cur_size -= 1
        if len(self) > 1:
            siftdown(self.vals, 0, self.cmp, len(self))
        return val
        
    def peek(self):
        assert len(self) > 0
        return self.vals[0]
        
    def push(self, val):
        assert not self.fixed_size or len(self) < self.max
        if self.fixed_size:
            self.vals[self.cur_size] = val
            self.cur_size += 1
        else:
            self.vals.append(val)
        if len(self) < 2:
            return
        siftup(self.vals, len(self) - 1, self.cmp)

    def is_valid(self, i=0):
        for i in non_leaf_nodes(len(self)):
            for child in children(i, len(self)):
                if self.cmp(self.vals[child], self.vals[i]) < 0:
                    return False
        return True
        
    def out(self):
        MAX_DIGITS = 3
        depth = math.floor(math.log(len(self), 2))
        leaves = 2 ** depth

        for i, val in enumerate(self.vals, start = 1):
            _cur_depth = math.log(i , 2)

            if _cur_depth % 1 == 0:
                cur_depth = math.floor(_cur_depth)
                max_descendant_per_level = leaves / 2.0 ** cur_depth
                width = int(max_descendant_per_level * MAX_DIGITS +
                            max_descendant_per_level - 1)
                print("\n")
            print(str(val).center(width), end = ' ')
        print()
        
def non_leaf_nodes(n):
    return range(n / 2 - 1, -1, -1)

'''
loose complexity is O(nlogn)
complexity (with careful analysis): O(n)
Analysis:
In a complete bin tree there are n/2 leaves and n/2 non leaves.
                    1                 1*log(n)
    /\              2                 2*(log(n)-1)
   /\/\             .                 .
  /\/\/\            .                 .
 /\/\/\/\           n/4               n/4 * 1
/\/\/\/\/\          n/2 (leaves)      n/2 * 0

Heapify starts siftdown from one level above the leaf level, since leaves are already heaps


watch from 35:00 for analysis
http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-4-heaps-and-heap-sort/

'''
def heapify(vals, cmp_):
    n = len(vals)
    for i in non_leaf_nodes(n):
        siftdown(vals, i, cmp_, n)
    return vals

def siftup(heap, i, cmp_):
    while True:
        p = parent(i)
        if cmp_(heap[i], heap[p]) < 0:
            heap[i], heap[p] = heap[p], heap[i]
        if p == 0:
            return
        i = p
        
#def siftdown(heap, i, cmp_, n):
#    mini = i
#    for child in children(i, n):
#        if cmp_(heap[mini], heap[child]) > 0:
#            mini = child
#    if i!=mini:
#        heap[i], heap[mini] = heap[mini], heap[i]
#        if mini < n / 2:
#            siftdown(heap, mini, cmp_, n)
def min_i(a, i, n, cmp_):
    l = i * 2 + 1
    r = l + 1
    min = i
    if l < n and cmp_(a[min], a[l]) > 0:
        min = l
    if r < n and cmp_(a[min], a[r]) > 0:
        min = r
    return min
    
def siftdown(heap, i, cmp_, n):
    m = min_i(heap, i, n, cmp_)
    if m != i:
        heap[i], heap[m] = heap[m], heap[i]
        if m < n / 2:
            siftdown(heap, m, cmp_, n)


def reverse_cmp(x, y): return -cmp(x, y)
    
def sort(a):
    heap = Heap(a, reverse_cmp, True)
    for i in a:
        heap.pop()
    

def main():
    a = arrays.make(sys.argv)
    sys.setrecursionlimit(2**31-1)
    sort(a)
    return a

if __name__=="__main__":
     main()
     #print(main())
else:
    
######################################## TESTS ##############################
    from numpy import random as rand
    def should_validate():
        heap =  Heap()
    
        heap.vals = [1, 3, 2, 4, 6, 8, 10, 7]
        assert heap.is_valid()
    
        heap.vals = range(100)
        assert heap.is_valid()
    
        heap.vals = [2, 3, 1]
        assert not heap.is_valid()
    
    def should_heapify():
        for i in range(3):
            heap = Heap(list(rand.randint(1000, size=100)))
            assert heap.is_valid()
    
    
    def should_add_and_delete():
        for i in range(3):
            vals = list(rand.randint(1000, size=200))
            heap = Heap()
            for i, val in enumerate(vals, start=1):
                heap.push(val)
                assert heap.peek() == min(vals[:i])
            assert heap.is_valid()
            for val in sorted(vals):
                assert heap.pop() == val
            assert not len(heap)
    
    def should_heap_sort():
        for n in [50, 100, 200, 500, 1000]:
            vals = list(rand.randint(10000, size=n))
            original = vals[:]
            heap = Heap(vals, lambda x, y: -cmp(x, y), True)
    
            for i in vals:
                heap.pop()
            assert sorted(original) == vals
    
