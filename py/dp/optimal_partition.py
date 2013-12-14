#partition an array into k parts such the difference between each part is minimized

from __future__ import division
import math
def partition(arr, k):
    assert k <= len(arr)
    ratio = sum(arr) / k
    max_part_val = int(math.ceil(ratio) if ratio - int(ratio) >= .5 else math.floor(ratio))
    parts = []
    dp_table = [[[] for i in range(len(arr) + 1)]  for j in range(max_part_val + 1)]
    for l in range(k - 1):
        for i in range(1, max_part_val + 1):
            for j in range(1, len(arr) + 1):
                if arr[j - 1] > i:
                    dp_table[i][j] = max([], dp_table[i][j - 1], key = sum)
                    continue
                dp_table[i][j] = max(dp_table[i - arr[j - 1]][j - 1] + arr[j - 1: j],
                                     dp_table[i][j - 1], key = sum)
        cur_partition = dp_table[max_part_val][len(arr)]
        parts.append(cur_partition)
        for e in cur_partition:
            arr.remove(e)
    parts.append(arr)
    return parts

def balanced_partition_diff(arr, k):
    parts = partition(arr, k)
    n = len(parts)
    max_diff = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_diff = max(max_diff, math.fabs(sum(parts[i]) - sum(parts[j])))
    return max_diff


############################## TESTS ##############################
def assert_array_equals(arr1, arr2):
    assert len(arr1) == len(arr2)
    arr2_sorted = map(sorted, arr2)
    for eles in map(sorted, arr1):
        assert eles in arr2_sorted
        arr2_sorted.remove(eles)
        
def should_parition():
    assert_array_equals([[3, 5, 9, 5, 3, 2], [10, 8, 7, 2]], 
                        partition([2, 10, 3, 8, 5, 7, 9, 5, 3, 2], 2))
    assert_array_equals([[1], [3]], 
                        partition([1, 3], 2))
    assert_array_equals([[9, 10], [4, 7, 8], [1, 3, 3, 5, 6]], 
                        partition([1, 3, 3, 4, 5, 6, 7, 8, 9, 10], 3))
    assert_array_equals([[1, 10], [3, 8], [4, 7], [5, 6], [3, 9]], 
                        partition([1, 3, 3, 4, 5, 6, 7, 8, 9, 10], 5))

    assert_array_equals([[3, 1, 1], [2, 2, 1]], 
                        partition([3, 1, 1, 2, 1, 2], 2))
    assert_array_equals([[1, 2], [ 1, 2], [3, 1]], 
                        partition([3, 1, 1, 2, 1, 2], 3))
    assert_array_equals([[1, 2], [1, 2], [3], [1]], 
                        partition([3, 1, 1, 2, 1, 2], 4))
            
    
def should_give_partition_diff():
    assert 0 == balanced_partition_diff([2, 10, 3, 8, 5, 7, 9, 5, 3, 2], 2)
    assert 2 == balanced_partition_diff([1, 3], 2)
    assert 1 == balanced_partition_diff([1, 3, 3, 4, 5, 6, 7, 8, 9, 10], 3)
    assert 1 == balanced_partition_diff([1, 3, 3, 4, 5, 6, 7, 8, 9, 10], 5)
            
    


            
                
            