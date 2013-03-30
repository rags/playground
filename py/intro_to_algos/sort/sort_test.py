from ds import arrays, heap
import selection_sort
import merge_sort
import quick_sort
import counting_sort
import quick_sort_functional
import numpy.random as rand
def _assert_sorted(a, original):
    assert sorted(original) == a

def _sort(algorithm, length):
    a = arrays.array(length,False)
    original = a[:]
    algorithm(a)
    return a, original

def test_sorting_works_for(algorithm):
    _assert_sorted(*_sort(algorithm,10))
    _assert_sorted(*_sort(algorithm,101))
    _assert_sorted(*_sort(algorithm,500))

def should_sort_with_selection_sort():
    test_sorting_works_for(selection_sort.sort)

def should_sort_with_heap_sort():
    test_sorting_works_for(heap.sort)

def should_sort_with_funtional_quick_sort():
    test_sorting_works_for(quick_sort_functional.sort)

def should_sort_with_merge_sort():
    test_sorting_works_for(merge_sort.sort)

def should_sort_with_quick_sort():
    test_sorting_works_for(quick_sort.sort)

def should_sort_with_quick_sort_with_dups():
    a = rand.randint(20, size=40).tolist()
    expected = sorted(a)
    quick_sort.sort(a)
    assert expected == a

def should_sort_with_counting_sort():
    test_sorting_works_for(counting_sort.sort)

def should_sort_duplicate_using_counting_sort():
    a = [2, 1, 1, 2, 2, 3, 4, 5]
    counting_sort.sort(a)
    assert sorted([2, 1, 1, 2, 2, 3, 4, 5]) == a
    
def should_sort_array_with_duplicate_using_counting_sort():
    copy = []
    copy[:] = arr = arrays.array(lower=10000, upper=30000) + arrays.array(lower=20000, upper=40000) + arrays.array(lower=1, upper=20000)
    counting_sort.sort(arr)
    assert not arr == copy
    assert arr == sorted(copy)

