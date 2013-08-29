'''
1) Indentify shapes in a matrix
2) Bucket shapes so that a relected/rotated shape that are essentially the same
   go into same bucket
'''
from __future__ import print_function
import itertools

def identify_and_bucket(matrix):
    shapes = identify_shapes(matrix)
    return bucket(shapes)

def bucket(shapes):
    buckets = map(lambda shape: [shape], shapes)
    i = 0
    while i < len(buckets):
        cur_path = path(buckets[i][0])
        j = i + 1
        while j < len(buckets):
            another_shape = buckets[j][0]
            if len(buckets[i][0]) == len(another_shape):
                if is_identical(cur_path, another_shape):
                    buckets[i].extend(buckets[j])
                    buckets.pop(j)
                    continue
            j += 1
        i += 1
    return buckets

    
def is_identical(diffs, shape):
    if diffs == path(shape) or diffs == path(map(lambda (x, y): (y, x), shape)):
        return True
    max_index = max(*shape[-1])
    return  (diffs == path(map(lambda (x, y): (max_index - x, max_index - y), shape)) or
             diffs == path(map(lambda (x, y): (x, max_index - y), shape)) or
             diffs == path(map(lambda (x, y): (max_index - x, y), shape)) or
             diffs == path(map(lambda (x, y): (max_index - y, max_index - x), shape)) or
             diffs == path(map(lambda (x, y): (y, max_index - x), shape)) or
             diffs == path(map(lambda (x, y): (max_index - y, x), shape)))
                      
def path(shape):
    shape.sort()
    return [(shape[i][0] - shape[i - 1][0], shape[i][1] - shape[i - 1][1]) for i in range(1, len(shape))]


def identify_shapes(matrix):
    n = len(matrix)
    shapes = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '1':
                shapes.append(collect_shape(matrix, i, j, n))
    return shapes

def collect_shape(matrix, i, j, n):
    co_ords = [(i, j)]
    matrix[i][j] = '0'
    if i + 1 < n and matrix[i + 1][j] == '1':
        co_ords.extend(collect_shape(matrix, i + 1, j, n))
    if j + 1 < n and matrix[i][j + 1] == '1':
        co_ords.extend(collect_shape(matrix, i, j + 1, n))
    if i - 1 > -1 and matrix[i - 1][j] == '1':
        co_ords.extend(collect_shape(matrix, i - 1, j, n))
    if j - 1 > -1 and matrix[i][j - 1] == '1':
        co_ords.extend(collect_shape(matrix, i, j - 1, n))
        
    return co_ords
        
1    
    
COLORS = map(lambda color: '\033[%sm' % color, range(90,97) + range(100,107) + range(31,37) + range(41,47))
NO_COLOR = '\033[0m'


############################## TESTS ##############################
import pytest

def build_matrix(str):
    return map(lambda line: list(line.strip()),str.split('\n'))
    
@pytest.mark.parametrize(('input', 'output'), [
    ('''00111
        10000
        10111
        10000
        00111''', [[[(0, 2), (0, 3), (0, 4)], [(1, 0), (2, 0), (3, 0)],
                   [(2, 2), (2, 3), (2, 4)], [(4, 2), (4, 3), (4, 4)]]]),
    
    ('''1000010011
        1001111001
        1100010001
        0001000010
        1011110010
        1001000011
        1000111000
        0010000100
        1110001111
        0001110100''',
     [[[(0, 0), (1, 0), (2, 0), (2, 1)], [(0, 8), (0, 9), (1, 9), (2, 9)],
       [(3, 8), (4, 8), (5, 8), (5, 9)], [(7, 2), (8, 0), (8, 1), (8, 2)]],
      
      [[(0, 5), (1, 3), (1, 4), (1, 5), (1, 6), (2, 5)],
       [(3, 3), (4, 2), (4, 3), (4, 4), (4, 5), (5, 3)],
       [(7, 7), (8, 6), (8, 7), (8, 8), (8, 9), (9, 7)]],
      
      [[(4, 0), (5, 0), (6, 0)], [(6, 4), (6, 5), (6, 6)], [(9, 3), (9, 4), (9, 5)]]]),
    
    ('''111101110101
        101000010101
        101001110010
        000000010010
        111100100100
        010100111101
        010100100101
        000011011010
        111000000010
        010100010101
        010100010101
        111001101111''',
     [[[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 2), (2, 0), (2, 2)],
       [(0, 5), (0, 6), (0, 7), (1, 7), (2, 5), (2, 6), (2, 7), (3, 7)],
       [(4, 0), (4, 1), (4, 2), (4, 3), (5, 1), (5, 3), (6, 1), (6, 3)],
       [(9, 9), (9, 11), (10, 9), (10, 11), (11, 8), (11, 9), (11, 10), (11, 11)]],
      
      [[(0, 9), (1, 9)], [(0, 11), (1, 11)], [(2, 10), (3, 10)], [(5, 11), (6, 11)],
       [(7, 4), (7, 5)], [(7, 7), (7, 8)], [(7, 10), (8, 10)], [(9, 3), (10, 3)],
       [(9, 7), (10, 7)], [(11, 5), (11, 6)]],

      [[(4, 6), (4, 9), (5, 6), (5, 7), (5, 8), (5, 9), (6, 6), (6, 9)],
       [(8, 0), (8, 1), (8, 2), (9, 1), (10, 1), (11, 0), (11, 1), (11, 2)]]
  ])
])
def should_identify_shapes(input, output):
    assert_has_same_shapes(output, identify_and_bucket(build_matrix(input)))

def assert_has_same_shapes(expected, actual):
    expected = sorted(map(lambda bucket: sorted(map(lambda shape: sorted(shape), bucket)), expected))
    expected = sorted(map(lambda bucket: sorted(map(lambda shape: sorted(shape), bucket)), actual))
    assert actual == expected

def main(matrix):
    buckets = identify_and_bucket(matrix)
    #print(buckets)
    n = len(matrix)
    out_matrix = [[('0', COLORS[0]) for i in range(n)] for i in range(n)]

    for i, bucket in enumerate(buckets):
        color = COLORS[(i + 8)% len(COLORS)]
        for x, y in itertools.chain(*bucket):
            out_matrix[x][y] = ('1', color)
    print("%s shapes found (grouped by color)" % len(buckets))
    for row in out_matrix:
        print()
        for val, color in row:
            print(color + val + ' ' + NO_COLOR, end = '')
    print('\n')
    
if __name__ == '__main__':
    strs = ['''111000010001000
              101110010001000
              111000111001111
              000010101000000
              000010111001111
              011110000001000
              000001011101000
              100101000001111
              100101111010000
              100100000010010
              111100011110010
              000011100000111
              101110100010101
              100011100010111
              100000011110000''',
            '''111101110101
               101000010101
               101001110010
               000000010010
               111100100100
               010100111101
               010100100101
               000011011010
               111000000010
               010100010101
               010100010101
               111001101111''',
            '''1000010011
               1001111001
               1100010001
               0001000010
               1011110010
               1001000011
               1000111000
               0010000100
               1110001111
               0001110100''']
    for str_ in strs:
        main(build_matrix(str_))
    