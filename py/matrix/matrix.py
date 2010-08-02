class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix
        self.__row_count_ = len(matrix)
        self.__col_count_ = len(matrix[0]) if self.__row_count_>0 else 0
        
    def multiply(self, matrix):
        return Matrix([[self.__multiply(matrix,j,i) for i in range(len(matrix[0])) ] for j in range(len(self.matrix))])
    
    def __multiply(self,matrix,i,j):
	return reduce(lambda sum, k: sum + self.matrix[i][k] * matrix[k][j],range(len(self.matrix[i])),0)

    def divide(self,num):
        return Matrix([[cell/float(num) for cell in row] for row in self.matrix ])

    def rows(self, index):
        return self.matrix[index]

    def columns(self, index):
       for i in range(self.__row_count_):
           yield rows(i)[j]
    
    def __str__(self):
        return str(self.matrix)

    def __eq__(self,matrix):
        return self.matrix == matrix or self.matrix == matrix.matrix

    def __getitem__(self, i):
        return self.matrix[i]

    def __len__(self):
        return len(self.matrix)
