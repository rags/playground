from cramer import *
from inverse import *
class TestLinearEquationSolver:
    def test_eq1(self):
        assert Matrix([[1],[-2],[3]]) == LinearEquationSolver().solve(Matrix([[2,1,1],[1,-1,-1],[1,2,1]]),Matrix([[3],[0],[0]]))

    def test_eq2(self):
        print LinearEquationSolver().solve(Matrix([[2,1,3],[2,6,8],[6,8,18]]),Matrix([[1],[3],[5]]))
        assert Matrix([[0.30000000000000004], [0.40000000000000013], [0.0]]) == LinearEquationSolver().solve(Matrix([[2,1,3],[2,6,8],[6,8,18]]),Matrix([[1],[3],[5]]))

    def test_eq3(self):
        assert Matrix([[5],[5],[-1.1102230246251565e-16],[2]]) == LinearEquationSolver().solve(Matrix([[1,-1,2,1],[1,1,-2,-2],[-3,3,2,2],[4,-4,-2,2]]),Matrix([[2],[6],[4],[4]]))
