from tree_stuff.Node import *
class BST:
    def __init__(self):
        self.__root__=None
    
    def insert(self,num):
        if self.__root__==None:
            self.__root__=Node(num)
            return
        self.__insert__(self.__root__,num)

    def __insert__(self,node,num):
        null_node_checker=lambda x:x==None
        if node.compare_data(lambda x: num>x):
            if node.compare_right(null_node_checker):
                node.set_right(Node(num))
                return
            self.__insert__(node.right(),num)
            return
        if node.compare_left(null_node_checker):
            node.set_left(Node(num))
            return
        self.__insert__(node.left(),num)
        return
    
    def __str__(self):
        return str(self.__root__)
        

def main():
    tree = BST()
    nums = [5,3,4,6,7,12,9,-1,2,1,15,20,18,8]
    map((lambda num: tree.insert(num)),nums)
    print tree

if __name__=='__main__':
    main()
    