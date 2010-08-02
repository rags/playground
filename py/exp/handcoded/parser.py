import re 
from common.nodes import *
class ShuntingYardParser:

    def __init__(self):
        self.expressions = []
        self.operators = []
        
    def make_tree(self,expression):
        for t in self.make_tokens(expression): print t
        for token in self.make_tokens(expression):
            self.simpleswitch(
                self.handle_low_precedence_op,
                self.push_op,                
                self.push_op,
                self.handle_close_braces).get(token,self.handle_operand)(token)       
        self.make_exp_while(self.has_ops)    
        return self.expressions.pop()
        
    def has_ops(self):
        return len(self.operators)>0

    def push_op(self,op):
        self.operators.append(op)

    def push_exp(self,exp):
        self.expressions.append(exp)

    def peek_op(self):
        return self.operators[-1]        
        
    def handle_operand(self,token):
        self.push_exp(Operand(token))

    def handle_low_precedence_op(self,token):
        precedence = self.precedence(token)
        self.make_exp_while(lambda:self.has_ops() and precedence<self.precedence(self.peek_op()))
        self.push_op(token)
        
    def handle_close_braces(self,token):
        self.make_exp_while(lambda:self.peek_op()!='(')
        self.operators.pop()

    def make_exp_while(self,predicate):
        while(predicate()):
            self.push_exp(self.make_operation())

    def make_operation(self):
        rhs,lhs = self.expressions.pop(),self.expressions.pop()
        return self.switch(AddOperator,
                           SubstractOperator,
                           MultiplyOperator,
                           DivideOperator)[self.operators.pop()](lhs,rhs)

    def precedence(self,operator):
        return self.simpleswitch(0,1)[operator]

    def simpleswitch(self,low_op_value,high_op_value,l_paren=None,r_paren=None):
        return self.switch(low_op_value,low_op_value,high_op_value,high_op_value,l_paren,r_paren)

    def switch(self,plus,minus,mult,div,l_paren=None,r_paren=None):
        return {'+':plus, '-':minus,  '*':mult,  '/':div,  '(':l_paren, ')':r_paren }

    def make_tokens(self,expression):
        i,n = 0,len(expression)
        while i<n:
            curChar = expression[i]
            match = re.match('\d+',curChar)
            if match==None:                
                assert re.match('[\+\-\*/\(\)]',curChar)!=None
                i += 1
                yield curChar
            else:                
                i += match.end()
                yield match.group(0)
