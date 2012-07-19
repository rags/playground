import selection_sort,unsorted,merge_sort
def _assert_sorted(a):
    for i in range(1,len(a)):
        assert a[i-1]<a[i]

def _sort(fn, length):
    a = unsorted.array(length)
    fn(a)
    return a

def should_sort_with_selection_sort():
    _assert_sorted(_sort(selection_sort.sort,10))
    _assert_sorted(_sort(selection_sort.sort,101))
    _assert_sorted(_sort(selection_sort.sort,500))

def should_sort_with_merge_sort():
    _assert_sorted(_sort(merge_sort.sort,10))
    _assert_sorted(_sort(merge_sort.sort,101))
    _assert_sorted(_sort(merge_sort.sort,500))

    
