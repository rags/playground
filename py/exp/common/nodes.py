class Operator:
	def __init__(self,lhs,rhs):
		self.lhs = lhs
		self.rhs = rhs

class AddOperator(Operator):    
	def visit(self,visitor):
		visitor.visitAddOperator(self)
class SubstractOperator(Operator):    
	def visit(self,visitor):
		visitor.visitSubstractOperator(self)
class MultiplyOperator(Operator):    
	def visit(self,visitor):
		visitor.visitMultiplyOperator(self)
class DivideOperator(Operator):    
	def visit(self,visitor):
		visitor.visitDivideOperator(self)

class Operand:
    def __init__(self,num):
        self.value = num
    
    def visit(self,visitor):
        visitor.visitOperand(self)

