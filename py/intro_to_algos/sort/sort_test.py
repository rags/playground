from ds import arrays
import selection_sort
import merge_sort
import quick_sort

def _assert_sorted(a):
    for i in range(1,len(a)):
        assert a[i-1]<a[i]

def _sort(algorithm, length):
    a = arrays.array(length,False)
    algorithm(a)
    return a

def test_sorting_works_for(algorithm):
    _assert_sorted(_sort(algorithm,10))
    _assert_sorted(_sort(algorithm,101))
    _assert_sorted(_sort(algorithm,500))

def should_sort_with_selection_sort():
    test_sorting_works_for(selection_sort.sort)

def should_sort_with_merge_sort():
    test_sorting_works_for(merge_sort.sort)

def should_sort_with_quick_sort():
    test_sorting_works_for(quick_sort.sort)


    
