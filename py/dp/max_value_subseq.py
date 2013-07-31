#T=O(n), S=O(n)
def max_val_space_n(a):
    max_ = [(a[0], (0, 0))]
    for i in range(1, len(a)):
        prev, (start, end)= max_[i - 1]
        max_.append(max((a[i], (i, i)), ((prev + a[i]), (start, i))))
    return max(max_)

#T=O(n), S=O(1)
def max_val(a):
    max_, max_so_far= a[0], a[0]
    start, end, start_so_far, end_so_far = 0, 0, 0, 0
    for i in range(1, len(a)):
        if max_so_far > 0:
            end_so_far = i
            max_so_far = a[i] +  max_so_far
        else:
             max_so_far = a[i]
             start_so_far = i
             end_so_far = i
        if max_so_far > max_:
            max_, start, end= max_so_far, start_so_far, end_so_far
            
    return max_, (start, end)

############################## TESTS ##############################
import pytest


@pytest.mark.parametrize('algo', [max_val, max_val_space_n])
def should_find_contigious_max_value_subseq(algo):
    assert (20, (1, 3)) == algo([-2, 11, -4, 13, -5, 2])
    assert (19, (2, 3)) == algo([5, -6, 7, 12, -3, 0, -11, -6])
    assert (30, (5, 6)) == algo([-15, 29, -36, 3, -22, 11, 19, -5])
    assert (3, (6, 6)) == algo([-5, -1, 2, -3, 0, -3, 3])
    
    