# http://en.wikipedia.org/wiki/Splay_tree

# The simpler version is bottom up which is essentially bst
# with splaying at the end of all operations (search, add remove)
# Bottom up needs 2 passes to balance and hence less optimal



from ds.nodes import DoubleLinkNode as Node
from bst import _find, next_descendant_in_order
from rbtree import rotate_left, rotate_right #rotation maintaining parents

def make_node(value, parent=None, left=None, right = None):
    node = Node(value, left, right)
    node.parent = parent
    return node
    
class SplayTree(object):
    def __init__(self, root=None):
        self.root = root
        
    def insert(self, val):
        root = self.root
        if not root:
            self.root = make_node(val)
            return
        node, parent = _find(root, val)
        if val < node.value:
            node.left = make_node(val, node)
            return self.splay(node.left)
        node.right = make_node(val, node, right=node.right)
        if node.right.right:
            node.right.right.parent = node.right
        self.splay(node.right)

    def find(self, val):
        node = _find(self.root, val)[0]
        self.splay(node)    
        if node.value == val:
            return node

    def delete(self, val):
        node, parent = _find(self.root, val)
        if not node.value == val:
            return
        if node.left and node.right:
            next_node, next_node_parent = next_descendant_in_order(node)
            node.value = next_node.value
            node, parent = next_node, next_node_parent
        #now the node will have at most 1 child (i.e 0 or 1 child)
        child = node.left if node.left else node.right
        if not parent:
            node.left = node.right = None
            if child:
                child.parent = None
            self.root = child
            return
        if parent.left == node:
            parent.left = child
        else:
            parent.right = child
        if child:
            child.parent = parent
        node.left = node.right = node.parent = None
        return self.splay(parent)

    def splay(self, node):

        while node.parent:
            parent, grandpa= node.parent, node.parent.parent
            if not grandpa:
                (rotate_right if parent.left == node else rotate_left)(parent)
                continue
            #has grand_parent
            rotate_fn = (double_rotate_right_zig_zig
             if grandpa.left == parent and parent.left == node
             else double_rotate_right_zig_zag
             if grandpa.left == parent and parent.right == node
             else double_rotate_left_zig_zig
             if grandpa.right == parent and parent.right == node
             else double_rotate_left_zig_zag
             if grandpa.right == parent and parent.left == node
             else None)
            assert rotate_fn, "N=%s P=%s G=%s\n %s" % (node.value,
                                                       parent.value,
                                                       grandpa.value,
                                                       strify(self.root))
            rotate_fn(grandpa, parent, node)

        self.root = node

def assign_parents(G, P, N):
    gg = G.parent
    if gg:
        if gg.left == G:
            gg.left = N
        else:
            gg.right = N
        N.parent = gg
    else:
        N.parent = None

    for node in [G, P, N]:
        for child in node.children:
            if child:
                child.parent = node
    
def double_rotate_right_zig_zig(G, P, N):
    P.left, G.left = N.right, P.right
    N.right, P.right = P, G
    assign_parents(G, P, N)        
    
def double_rotate_left_zig_zig(G, P, N):
    P.right, G.right = N.left, P.left
    N.left, P.left = P, G
    assign_parents(G, P, N)        


def double_rotate_left_zig_zag(G, P, N):
    G.right, P.left = N.left, N.right
    N.left, N.right = G, P
    assign_parents(G, P, N)
    
def double_rotate_right_zig_zag(G, P, N):
    G.left, P.right = N.right, N.left
    N.right, N.left = G, P
    assign_parents(G, P, N)

        
######################################## TESTS ########################################
def N(val, l=None, r=None):
    node = make_node(val, left=l, right=r)
    if l:
        l.parent = node
    if r:
        r.parent = node
    return node


    
from tree_ops import inorder, depth
import numpy
from numpy import random as rand
def should_splay():
    tree = SplayTree(N(6, N(5, N(4, N(3, N(2, N(1)))))))
    tree.find(1)
    assert [1, 2, 3, 4, 5, 6] == inorder(tree.root)
    assert tree.root.value == 1
    tree.delete(4)
    assert [1, 2, 3, 5, 6] == inorder(tree.root)

def should_insert_delete():
    for i in range(5):#regress 5 times
        depth_ratio = 0
        NO_OF_TREES = 25
        for i in range(NO_OF_TREES):
            tree = SplayTree()
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
    tree = SplayTree()
    elems = [31, 13, 98, 17, 13, 9, 2, 2, 2, 90, 36]
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

def strify(node):
    valstr = "%s" % ((node.value, id(node)),)
    if not(node.left or node.right):
        return "(%s%s)" % (valstr, (", P=%s" % ((node.parent.value, id(node.parent)),) ) if node.parent else '') 
    return "(%s%s%s%s)" % (
        valstr,
        (", L=%s" % strify(node.left)) if node.left else '', 
        (", R=%s" % strify(node.right)) if node.right else '',
        (", P=%s" % ((node.parent.value, id(node.parent)),) ) if node.parent else '')
