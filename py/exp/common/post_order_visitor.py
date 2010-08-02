class PostOrderVisitor:

	def __init__(self):
		self.__instructions__ = []

	def visitOperand(self,node):
		self.__instructions__.append("PUSH " + str(node.value))

	def visitAddOperator(self,node):
		self.__visitChildren__(node)
		self.__instructions__.append("ADD")
	
	def visitSubstractOperator(self,node):
		self.__visitChildren__(node)
		self.__instructions__.append("SUB")
	
	def visitMultiplyOperator(self,node):
		self.__visitChildren__(node)
		self.__instructions__.append("MUL")
	
	def visitDivideOperator(self,node):
		self.__visitChildren__(node)
		self.__instructions__.append("DIV")
	
	def __visitChildren__(self,node):
		node.lhs.visit(self)
		node.rhs.visit(self)
		
	def instruction_set(self):
		return self.__instructions__
