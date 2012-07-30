import numpy
import math

def _dimensions(matrix):
    rows = len(matrix)
    return (rows,0 if rows==0 else len(matrix[0]))

def _minimum_square_matrix_dimensions_for(num):
    return int(2 ** math.ceil(numpy.log2(num)))

def _pad_to_extend(matrix, n):
    col_len = len(matrix[0])
    if(col_len<n):
        col_padding = [0]*(n-col_len)
        for row in matrix:
            row.extend(col_padding)

    row_len = len(matrix)
    if(row_len<n):
        row_padding = [0]*n
        for i in xrange(n-row_len):
            matrix.append(row_padding)

def multiply(matrix1,matrix2):
    m1,n1 = _dimensions(matrix1)
    m2,n2 = _dimensions(matrix2)
    if(m1<1 or n1<1 or m2<1 or m2 < 1):
           return [[]]
    upper_bound = _minimum_square_matrix_dimensions_for(max(m1,n1,m2,n2))
    _pad_to_extend(matrix1,upper_bound)
    _pad_to_extend(matrix2,upper_bound)
    result = _multiply(matrix1,matrix2)

    return map(lambda row: row[:n2],result[:m1])

def _multiply(a,b):
    n = len(a)
    if n==1:
        return [[a[0][0] * b[0][0]]]
    a00, a01, a10, a11 = [],[],[],[]
    b00, b01, b10, b11 = [],[],[],[]
    mid = n//2
    for i in xrange(mid):
        a00.append([])
        a01.append([])
        a10.append([])
        a11.append([])
        b00.append([])
        b01.append([])
        b10.append([])
        b11.append([])
        for j in xrange(mid):
            a00[i].append(a[i][j])
            a01[i].append(a[i][j+mid])
            a10[i].append(a[i+mid][j])
            a11[i].append(a[i+mid][j+mid])
            b00[i].append(b[i][j])        
            b01[i].append(b[i][j+mid])    
            b10[i].append(b[i+mid][j])    
            b11[i].append(b[i+mid][j+mid])
    
    p1 = _multiply(a00, substract(b01, b11)) 
    p2 = _multiply(add(a00, a01), b11)
    p3 = _multiply(add(a10, a11), b00)
    p4 = _multiply(a11, substract(b10, b00))
    p5 = _multiply(add(a00, a11), add(b00, b11))
    p6 = _multiply(substract(a01, a11), add(b10, b11))
    p7 = _multiply(substract(a00, a10), add(b00, b01))

    c00 = add(substract(add(p5,p4),p2),p6)
    c01 = add(p1,p2)
    c10 = add(p3,p4)
    c11 = substract(substract(add(p5,p1),p3),p7)
    c = [[0 for i in xrange(n)] for j in xrange(n)]

    for i in xrange(mid):
        for j in xrange(mid):
            c[i][j] = c00[i][j]
            c[i][j + mid] = c01[i][j]
            c[i + mid][j] = c10[i][j]
            c[i + mid][j + mid] = c11[i][j]

    return c

def add(matrix1, matrix2):
    return _operation(matrix1, matrix2, lambda a,b:a+b)

def substract(matrix1, matrix2):
    return _operation(matrix1, matrix2, lambda a,b:a-b)

def _operation(matrix1,matrix2,op):
    m = len(matrix1)
    n = len(matrix1[0])
    return [[op(matrix1[i][j],matrix2[i][j]) for j in xrange(n)] for i in xrange(m)]

def exp(matrix,n):
    if n==0:
     return [[0]*len(matrix[0])]*len(matrix)
    if n==1:
        return matrix
    exp_n_by_2 = exp(matrix,n//2)
    result = multiply(exp_n_by_2,exp_n_by_2)
    return result if n%2==0 else multiply(result,matrix)

########################################tests########################################

def should_pad_to_extend_matrix():
    assert square_matrix([[1,2]],2) == [[1,2],[0,0]]
    assert square_matrix([[1],[2]],2) == [[1,0],[2,0]]

def should_calcualte_the_nearest_square_matrix_dimesnion():
    assert _minimum_square_matrix_dimensions_for(3)==4
    assert _minimum_square_matrix_dimensions_for(63)==64
    assert _minimum_square_matrix_dimensions_for(67)==128

def square_matrix(m,dim):
    _pad_to_extend(m,dim)
    return m

def should_multiply_upto_2_x_2():
    assert multiply([[2]],[[3]])==[[6]]    
    assert multiply([[2],[3]],[[3]])==[[6],[9]]    
    assert multiply([[3,4]],[[2],[3]])==[[18]]
    assert multiply([[3,4],[5,6]],[[2],[3]])==[[18],[28]]
    assert multiply([[3,4],[5,6]],[[2,1],[3,1]])==[[18,7],[28,11]]

def should_multiply_rectangular_matrices():
    assert multiply([[1, 4], [6, -3], [7, 2]], [[8, 9], [-2, 4]]) == [[0, 25], [54, 42], [52, 71]]
    assert multiply([[-3, 0, 1], [5, 4, 6]], [[7, -2, 0, 8], [3, -1, 1, 2], [4, -4, 5, 6]]) == [[-17, 2, 5, -18], [71, -38, 34, 84]]
    assert multiply([[1]*4]*4,[[1]*4]*4) == [[4]*4]*4
    assert multiply([[-1]*3]*3,[[-1]*3]*3) == [[3]*3]*3

def should_calculate_exponents():
    m = [[-1, -1, -1,-1], 
         [-1, -1, -1,-1], 
         [-1, -1, -1,-1], 
         [-1, -1, -1,-1]]
    assert exp(m,2) == [[4]*4]*4
    assert exp(m,3) == [[-16]*4]*4

def should_exp_3x3():
    m = [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]
    #todo: trim extra 0's for odd exponents
    assert exp(m,3) == [[9, 9, 9, 0],
                        [9, 9, 9, 0],
                        [9, 9, 9, 0]]
    
    
