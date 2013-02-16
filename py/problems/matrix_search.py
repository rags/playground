def search(matrix, element):
    assert len(matrix) > 0
    assert len(matrix[0]) > 0
    return _search(matrix, element, (0, 0), (len(matrix), len(matrix[0])))

'''
Search a matrix that has all rows sorted left to right and all columns sorted top to bottom
    [ -5,  -2,  -1,   4,   7,   9]
    ------------------------------
-7  [-12,  -9,  -8,  -3,   0,   2]
-4  [ -9,  -6,  -5,   0,   3,   5]
 1  [ -4,  -1,   0,   5,   8,  10]
 5  [  0,   3,   4,   9,  12,  14]
 6  [  1,   4,   5,  10,  13,  15]
 8  [  3,   6,   7,  12,  15,  17]

'''

def _search(matrix, ele, (i, j), (m, n)):
    if i >= m or j >= n:
        return
    row_idx = (i + m) / 2
    row = matrix[row_idx]
    col_idx = bs(row, j, n, ele)
    if row[col_idx] == ele:
        return (row_idx, col_idx)
    if row[col_idx] > ele:
        return (_search(matrix, ele, (i, j), (row_idx, col_idx))
                or
                _search(matrix, ele, (row_idx, j), (m, col_idx))
                or
                _search(matrix, ele, (i, col_idx), (row_idx, n)))
        
    return (_search(matrix, ele, (i, col_idx + 1), (row_idx + 1, n))
            or
            _search(matrix, ele, (row_idx + 1, col_idx + 1), (m, n))
            or
            _search(matrix, ele, (row_idx + 1, j), (m, col_idx + 1)))
    


def bs(arr, low, high, ele):
    assert low <= high - 1
    if low == high - 1:
        return low
    mid = (low + high) / 2
    if ele == arr[mid]:
        return mid
    if ele > arr[mid]:
        if mid + 1 == high:
            return mid
        return bs(arr, mid + 1, high, ele)
    return bs(arr, low, mid, ele)
    

import numpy.random as rand
import numpy as np
def should_search_a_sorted_matrix():
    for i in range(3):
        arr1 = rand.randint(100, size=16)
        arr2 = rand.randint(100, size=24)
        arr1.sort()
        arr2.sort()
        matrix1 = np.resize(arr1, (4, 4)).tolist()
        matrix2 = np.resize(arr2, (6, 4)).tolist()
        for i in range(3):
            assert search(matrix1, arr1[rand.randint(0, len(arr1))])
            assert search(matrix2, arr2[rand.randint(0, len(arr2))])
            not_present = rand.randint(100, 200)
            assert not search(matrix1, not_present)
            assert not search(matrix2, not_present)
            


    

    
        
    

    