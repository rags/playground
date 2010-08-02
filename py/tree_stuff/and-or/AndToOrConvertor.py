from tree_stuff.Node import *
class AndToOrConvertor:
    def __init__(self,node):
        self.__node = node

    def convert(self):
       return self.__or_the_ands(self.__traverse(self.__node))

    def __traverse(self,node):
        if(isinstance(node,And)):
            return self.__and_node(node)
        if(isinstance(node,Or)):
            return self.__or_node(node)
        if(isinstance(node,Node)):
            return self.__data_node(node)
    
    def __and_node(self,node):
        leftors = self.__traverse(node.left())
        rightors = self.__traverse(node.right())
        return self.__and_the_ors(leftors,rightors)
        
    def __or_node(self,node):
        ors = self.__traverse(node.left())
        ors[len(ors):] = self.__traverse(node.right())
        return ors

    def __data_node(self,node):
        return [node]

    def __and_the_ors(self,leftors,rightors):
        ands = [And(left_node,right_node) for left_node in leftors for right_node in rightors]
        return ands

    def __or_the_ands(self,ands):
        return reduce(lambda x,y: Or(x,y),ands)

            
    
        
    