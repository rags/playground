import numpy.random as rand
'''
complexity:
assuming that array gets divided into half each time
T(n) + T(n/2) + T (n/4) ...... T
T(n (1+1/2+1/4+1/8+1/16....))
T(2n)

assuming random pivot:
T(n) <= f(n) <= T(2n)

f(n) = O(n)
'''
def find(arr, n, highest=True):
    assert arr
    assert n <= len(arr)
    n = len(arr) - n if highest else n - 1
    low, high = 0, len(arr) - 1
    return  partition(arr, low, high, n)

def partition(arr, low, high, n):
    rand_idx = rand.randint(low=low, high=high + 1)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
    i, j, pivot = low, high, arr[high]

    while i < j:
        while i < j and arr[i] < pivot: i += 1
        while i < j and arr[j] >= pivot: j -= 1
        if i < j: arr[i], arr[j] = arr[j], arr[i]

    if j == n:
        return pivot
    arr[j], arr[high]= pivot, arr[j]
    if j > n:
        return partition(arr, low, j - 1, n)
    return partition(arr, j + 1, high, n)


def should_find_with_dups():
    a = [1,  6,  0,  7,  5,  8,  7,  9,  8,  8]
    assert 8 == find(a, 2) == find(a, 3) == find(a, 4)
    assert 7 == find(a, 5) == find(a, 6) 
    assert 0 == find(a, 1, False)
    assert 7 == find([7, 7, 7, 7, 7], 3)
    assert 8 == find([7, 7, 7, 7, 8], 1)
    assert 7 == find([7, 7, 7, 7, 8], 2)
    assert 7 == find([7, 7, 7, 7, 8], 1, False)
    assert 7 == find([7], 1, False) ==  find([7], 1)
    
def should_return_nth_highest_or_lowest():
    for i in range(5):
        arr = rand.randint(2000, size=2000).tolist()
        copy = arr[:]
        copy.sort()
        print arr

        for i in range(3):
            n = rand.randint(low=1, high=2000)
            assert copy[-n] == find(arr, n)
            assert copy[n - 1] == find(arr, n, False)
            

if __name__ == '__main__':
    should_return_nth_highest_or_lowest()
        