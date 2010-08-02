import sys
from common.post_order_visitor import *
from antlrparser.parser import *
from handcoded.parser import *

def instructions_for(expression,parser):
    visitor = PostOrderVisitor()
    parser.make_tree(expression).visit(visitor)
    return visitor.instruction_set()

def instructions_str_for(expression,parser):
    return '\n'.join(instructions_for(expression,parser))

if __name__ == "__main__":
    input = raw_input()
    print "handcoded parser: \n" + instructions_str_for(input,ShuntingYardParser())
    print "parser generated from antlr grammer:\n" + instructions_str_for(input,AntlrParser())


