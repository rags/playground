# http://en.wikipedia.org/wiki/Splay_tree
# Top-down (rebalance as you go down) splay tree. Top down splay tree rebalances as you go and hence only 1 pass is required


from ds.nodes import DoubleLinkNode as Node

# removing dups b/w this method and splay makes code harder to reason about
# not worth the effort
def splay_left_most(node):
    right, right_left_most = None, None
    while node.left:
        if node.left.left:
            child, grandchild = node.left, node.left.left
            child.right, node.left = node, child.right
            new_left_most= child
            node = grandchild
        else:
            new_left_most = node
            node = node.left
        if not right_left_most:
            right = right_left_most = new_left_most
        else:
            right_left_most.left, new_left_most.left, right_left_most = (
                new_left_most, None, new_left_most)
    if right_left_most:
        right_left_most.left = node.right
    else:
        right = node.right
    node.right = right
    return node
                        
def splay(node, val, for_insert = False):
    left, left_right_most = None, None
    right, right_left_most = None, None
    while node:
        if val == node.value and not for_insert:
            break

        if val < node.value:
            if not node.left:
                if not for_insert:
                    break
            if node.left and val < node.left.value and node.left.left: #zig-zig
                child, grandchild = node.left, node.left.left
                child.right, node.left = node, child.right
                new_left_most= child
                node = grandchild
            else: #zig
                new_left_most = node
                node = node.left
            if not right_left_most:
                right = right_left_most = new_left_most
            else:
                right_left_most.left, new_left_most.left, right_left_most = (
                    new_left_most, None, new_left_most)
            continue
        if not node.right and not for_insert:
            break
        if node.right and val > node.right.value and node.right.right: #zig-zig
            child, grandchild = node.right, node.right.right
            child.left, node.right = node, child.left
            node = grandchild
            new_right_most= child
        else: #zig
            new_right_most = node
            node = node.right

        if not left_right_most:
            left = left_right_most = new_right_most
        else:
            left_right_most.right, new_right_most.right, left_right_most = (
                new_right_most, None, new_right_most)
    if not node:
        if not for_insert:
            return None
        node = Node(val)
    if left_right_most:
        left_right_most.right = node.left
    else:
        left = node.left
    if right_left_most:
        right_left_most.left = node.right
    else:
        right = node.right
        
    node.left, node.right = left, right
    return node

class Tree():
    def __init__(self, node=None):
        self.root = node
        
    def find(self, val):
        self.root = splay(self.root, val)
        if self.root and self.root.value == val:
            return self.root
        return None
        
    def insert(self, val):
        self.root = splay(self.root, val, True)
            
    def delete(self, val):
        if not self.root:
            return
        self.root = splay(self.root, val)
        if self.root.value != val:
            return
        if self.root.left and self.root.right:
            left = self.root.left
            self.root = splay_left_most(self.root.right)
            assert not self.root.left
            self.root.left = left
            return
        if self.root.left:
            self.root.left, self.root = None, self.root.left
        else:
            self.root.right, self.root = None, self.root.right
            
######################################## TESTS ########################################
N = Node
from tree_ops import inorder
#from bst import  is_valid_binary_tree
def should_splay():
    tree = N(6, N(5, N(4, N(3, N(2, N(1))))))
    tree = splay(tree, 1)
    assert tree.value == 1
    assert [1, 2, 3, 4, 5, 6] == inorder(tree)

def should_splay_tree():
    n = 20
    tree = None
    for i in range(n):
        tree = N(i, tree)
    for j in range(1, n):
        tree = splay(tree,j)
        assert tree.value == j
        assert range(n) == inorder(tree)
    
def should_splay_large_tree():
    tree = splay(large_tree(), 12)
    assert tree.value == 12
    assert inorder(tree) == inorder(large_tree())
    
def large_tree():
    return N(2,
             N(1),
             N(33,
               N(32,
                 N(31,
                   N(29,
                     N(27,
                       N(6,
                         N(4,
                           N(3),
                           N(5)),
                         N(25,
                           N(23,
                             N(21,
                               N(19,
                                 N(17,
                                   N(15,
                                     N(8,
                                       N(7),
                                       N(10,
                                         N(9),
                                         N(12,
                                           N(11),
                                           N(14, N(13), N(15))))),
                                     N(16)),
                                   N(18)),
                                 N(20)),
                               N(22)),
                             N(24)),
                           N(26))),
                       N(28)), N(30)),
                   N(32))),
               N(34)))
    #assert is_valid_binary_tree(tree)

from tree_ops import depth
import numpy
from numpy import random as rand

def should_insert_delete():
    for i in range(5):#regress 5 times
        depth_ratio = 0
        NO_OF_TREES = 25
        for i in range(NO_OF_TREES):
            tree = Tree()
            n = rand.randint(50, 250)
            elems = rand.randint(1, 100, size=n)
            for e in elems:
                tree.insert(e)
            assert inorder(tree.root) == sorted(elems)
            depth_ratio += depth(tree.root) / numpy.log2(n)
            for i in range(n // 2):
                tree.delete(elems[i])
            assert inorder(tree.root) == sorted(elems[n//2:])
            depth_ratio += depth(tree.root) / numpy.log2(n//2)

        # for NO_OF_TREES*2 no of samples the sample tree depth is atmost 2.5logn
        # i.e depth is order log(n) for splay trees 
        assert depth_ratio / (NO_OF_TREES * 2) < 2.5

def should_handle_dups():
    tree = Tree()
    elems = [31, 13, 98, 17, 13, 9,2, 2, 2, 90, 36]
    for e in elems:
        tree.insert(e)
    node = tree.find(98)
    assert inorder(node) == sorted(elems)
    assert node.value == 98
    assert tree.root.value == 98
    for i in range(len(elems)):
        tree.delete(elems[i])
        assert inorder(tree.root) == sorted(elems[i + 1:])
    assert not tree.root
    