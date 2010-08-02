from tree_stuff.Node import *
from AndToOrConvertor import *

def main():
    tree = And(Or(Node('a'),Node('b')),And(Or(Node('c'),Node('d')),Or(Node('e'),Node('f'))))
    print tree
    print AndToOrConvertor(tree).convert()

if  __name__ == '__main__':
    main()

    