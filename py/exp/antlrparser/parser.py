import sys
import antlr3
import antlr3.tree
from generated.ExpLexer import ExpLexer
from generated.ExpParser import ExpParser
from generated.ExpTreeParser import ExpTreeParser

class AntlrParser:

   def make_tree(self,expression):
      tokens = antlr3.CommonTokenStream(ExpLexer(antlr3.ANTLRStringStream(expression)))
      nodes = antlr3.tree.CommonTreeNodeStream(ExpParser(tokens).low_precedence_exp().tree)
      nodes.setTokenStream(tokens)   
      return ExpTreeParser(nodes).exp()



      
