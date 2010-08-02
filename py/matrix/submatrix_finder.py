class SubmatrixFinder:
    def __init__(self, matrix):
	self.__matrix__ = matrix
   
    def submatrix(self, row, col):
        return [[self.__matrix__[i][j] for j in self.__filter__(col)] for i in self.__filter__(row)]

    def __filter__(self,index):
	return filter(self.__index_not_eq__(index),range(len(self.__matrix__)))		
	
    def __index_not_eq__(self,index):
	return lambda i: i!=index 			        
	
        
