from submatrix_finder import *
from matrix import *

class TestSubmatrixFinder:
    def test_3_x_3(self):
        submatrix_finder = SubmatrixFinder(Matrix([[1,2,3],[4,5,6],[7,8,9]]))
        assert [[5,6],[8,9]] == submatrix_finder.submatrix(0,0)
        assert [[4,6],[7,9]] == submatrix_finder.submatrix(0,1)
        assert [[4,5],[7,8]] == submatrix_finder.submatrix(0,2)    
        
        assert [[2,3],[8,9]] ==  submatrix_finder.submatrix(1,0)
        assert [[1,3],[7,9]] ==  submatrix_finder.submatrix(1,1)
        assert [[1,2],[7,8]] ==  submatrix_finder.submatrix(1,2)    
        
        
        assert [[2,3],[5,6]] ==  submatrix_finder.submatrix(2,0)
        assert [[1,3],[4,6]] ==  submatrix_finder.submatrix(2,1)
        assert [[1,2],[4,5]] ==  submatrix_finder.submatrix(2,2)    
        

