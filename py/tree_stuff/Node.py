class Node:
    "foo"
    def __init__(self, data,left=None,right=None):
        self.__data,self.__left,self.__right=data,left,right
    
    def __str__(self):
        return  (str(self.__left) if isinstance(self.__left,Node) else '')+' ' + str(self.__data) + ' ' + (str(self.__right) if isinstance(self.__right,Node) else '')

    def left(self):
        return self.__left

    def right(self):    
        return self.__right
    
    def set_left(self,left):
        self.__left=left

    def set_right(self,right):    
        self.__right = right
    
    def compare_data(self,fn):
        return fn(self.__data)
    def compare_left(self,fn):
        return fn(self.__left)
    def compare_right(self,fn):
        return fn(self.__right)

class And(Node):
    def __init__(self,left=None,right=None):
        Node.__init__(self,'&',left,right)

class Or(Node):
    def __init__(self,left=None,right=None):
        Node.__init__(self,'|',left,right)

    def __str__(self):
        return '(' + Node.__str__(self) + ')'

