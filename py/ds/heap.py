from __future__ import print_function
import math
from ds import arrays
import sys
        
def parent(i):
    assert i > 0
    return (i - 1) // 2
def left(i): return i * 2 + 1
def right(i): return i * 2 + 2

def children(i, size=None):
    l, r = left(i), right(i)
    return (l, r) if not size else (i for i in (l, r) if i < size)

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

        for i, val in enumerate(self.vals):
            _cur_depth = math.log(i + 1, 2)

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
        
def siftdown(heap, i, cmp_, n):
    for child in children(i, n):
        if cmp_(heap[i], heap[child]) > 0:
            heap[i], heap[child] = heap[child], heap[i]
            if i < n / 2:
                siftdown(heap, child, cmp_, n)

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
        for i, val in enumerate(vals):
            heap.push(val)
            assert heap.peek() == min(vals[:i+1])
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

