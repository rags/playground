from matrix import *
from itertools import *
class TestMatrix:
    def test_multiply_3_x_3_X_3_x_4(self):
        assert Matrix([[17, 23, 35, 41], [41, 56, 83, 98], [65, 89, 131, 155]]) == Matrix([[1,2,3],[4,5,6],[7,8,9]]).multiply(Matrix([[1,2,3,4],[5,6,7,8],[2,3,6,7]]))

    def test_multiply_4_x_4_X_1_x_4(self):
        assert Matrix([[30],[40],[58],[59]]) == Matrix([[1,2,3,4],[4,5,6,2],[7,8,9,2],[3,5,6,7]]).multiply([[1],[2],[3],[4]])
        
    def test_to_string(self):
        assert str(Matrix([[1,2,3],[4,5,6],[7,8,9]])) == '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]'

    def test_columns(self):
        assert (lambda result,tuple: result and  tuple[0]==tuple[1], izip([1,2,3,4],Matrix([[2,1,3],[4,2,4],[2,3,4],[1,4,5]]).columns(1)))
        
    def test_divide(self):
        print Matrix([[1,2,3],[4,5,6],[7,8,9]]).divide(2)
        assert Matrix([[.5,1,1.5],[2,2.5,3],[3.5,4,4.5]])==Matrix([[1,2,3],[4,5,6],[7,8,9]]).divide(2)
