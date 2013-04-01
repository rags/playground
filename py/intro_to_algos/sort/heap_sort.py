import sys
from ds import arrays
from profile import profile

def heapify(vals):
    n = len(vals)
    i = n // 2 - 1
    while i >= 0:
        siftdown(vals, i, n)
        i -= 1
    return vals

@profile
def sort(a):
    heapify(a)
    i = len(a) - 1
    while i > 0:
        a[0], a[i] = a[i], a[0]
        i -= 1
        siftdown(a, 0, i + 1)
    
def siftdown(heap, i, n):
    max = i
    l = 2 * i + 1
    if l < n and heap[l] > heap[max]:
        max = l
    r = l + 1
    if r < n and heap[r] > heap[max]:
        max = r

    if max != i:
        heap[i], heap[max] = heap[max], heap[i]
        if max < n / 2:
            siftdown(heap, max, n)


def main():
    a = arrays.make(sys.argv)
    sys.setrecursionlimit(2**31-1)
    sort(a)
    return a

if __name__=="__main__":
    main()
    