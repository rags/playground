from determinant import *
from submatrix_finder import *
from matrix import *
class InverseFinder:
    def inverse(self,matrix):
        return AdjointFinder(matrix).adjoint().divide(DeterminantCalculator().determinant(matrix))

class AdjointFinder:
    def __init__(self,matrix):
	self.__matrix__ = matrix
	self.__submatrix_finder__ = SubmatrixFinder(matrix)
        self.__deteminant_calculator__ = DeterminantCalculator()

    def adjoint(self):
        if len(self.__matrix__)==1: 
            return [[self.__matrix__[0][0]]]
        indices = range(len(self.__matrix__))
        return Matrix([[self.__cofactor__(j,i) for j in indices] for i in indices])
	
    def __cofactor__(self, i, j):
	return MatrixUtil().sign(i,j) * self.__deteminant_calculator__.determinant(self.__submatrix_finder__.submatrix(i,j)) 
        
        
