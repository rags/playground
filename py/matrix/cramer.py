from inverse import *

class LinearEquationSolver:
    def solve(self,coefficients,result):
        return InverseFinder().inverse(coefficients).multiply(result)
