from determinant import *
from matrix import *

class TestDeterminantCalculator:
    def test_determinant(self):
        determinant_calculator = DeterminantCalculator()
        assert 23  == determinant_calculator.determinant(Matrix([[23]]))
        assert -2  == determinant_calculator.determinant([[2,3],[4,5]])
        assert 0  == determinant_calculator.determinant([[1,2,3],[4,5,6],[7,8,9]])
        assert 313  == determinant_calculator.determinant(Matrix([[4,5,6,7],[1,4,6,7],[3,4,5,8],[3,9,0,1]]))
    
    def test_sign(self):
        util = MatrixUtil()
        assert 1==util.sign(0,0)
        assert -1==util.sign(0,1)
        assert 1==util.sign(0,2)
        assert -1==util.sign(0,3)
        
        assert -1==util.sign(1,0)
        assert 1==util.sign(1,1)
        assert -1==util.sign(1,2)
        assert 1==util.sign(1,3)

        assert -1==util.sign(3,0)
        assert 1==util.sign(3,1)
        assert -1==util.sign(3,2)
        assert 1==util.sign(3,3)
        assert -1==util.sign(3,4)


