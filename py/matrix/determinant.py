from submatrix_finder import *
class DeterminantCalculator:
    def determinant(self, matrix):
        if len(matrix)==1: 
            return matrix[0][0]
        determinant=0
        util = MatrixUtil()
        for i in range(len(matrix)):
            determinant = determinant + \
                          util.sign(0,i) * matrix[0][i] * \
                          self.determinant(self.__submatrix__(matrix,i))
        return determinant
            
    def __submatrix__(self,matrix,index):
        return SubmatrixFinder(matrix).submatrix(0,index)

class MatrixUtil:
    def sign(self,i,j):
        return 1 if (i+j)%2==0 else -1
