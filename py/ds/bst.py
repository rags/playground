from nodes import DoubleLinkNode as Node
from tree_ops import inorder

def insert_node(new_node, tree=None):
    if not tree:
        return new_node
    value = new_node.value
    node = _find(tree, value)[0]
    if node.value == value:
        new_node.right = node.right
        node.right = new_node
        return tree
    if node.value > value:
        node.left = new_node
    else:
        node.right = new_node
    return tree

def insert(value, tree=None):
    insert_node(Node(value), tree)
    
def search(tree, value):
    node = _find(tree, value)[0]
    return node.value == value

def is_valid_binary_tree(tree):
    values_in_order = inorder(tree)
    return values_in_order == sorted(values_in_order)
    
def _find(node, value, parent=None):
    if not node:
        raise Exception("empty node")
    if node.value > value and node.left:
        return _find(node.left, value, node)
    if node.value < value and node.right:
        return _find(node.right, value, node)
    return (node, parent)

def nth_highest(tree, n):

    def _preorder(node, n, cnt):
        if node.right:
            cnt, val = _preorder(node.right, n, cnt)
            if val:
                return cnt, val
        cnt += 1
        if cnt == n:
            return cnt, node.value
        if node.left:
            cnt, val = _preorder(node.left, n, cnt)
            if val:
                return cnt, val
        return cnt, None
    return _preorder(tree, n, 0)[1]
    
def left_most(node, parent):
    while(node.left):
        parent = node
        node = node.left
    return node, parent
    
def next_descendant_in_order(node):#left most child in the right branch of the node is the next number in sequence
    if not node.right:
        return None, None
    return left_most(node.right, node)
    
def delete(tree, value):
    node, parent= _find(tree, value)
    if node.value != value:
        return tree
    if not (node.right and node.left): # the node has either one or no children
        return delete_node_with_1_or_0_children(parent, node,
                                                node.right or node.left or None, tree)

    #node has both children
    next_node, next_node_parent = next_descendant_in_order(node)
    node.value = next_node.value #over write with next number in sequence
    #del next_node. This node may have a right child, but not left as its the left most node
    next_node_parent.left = next_node.right 
    return tree

def delete_node_with_1_or_0_children(parent, node, grand_child, root):
    if not parent and node == root: # it's a root node
        node.right = node.right = None
        return grand_child
    if node == parent.right:
        parent.right = grand_child
    else:
        parent.left = grand_child
    return root

def lca(tree, v1, v2):
    def _lca(node,v1, v2):
        if not node:
            return
        if v1 > node.value and v2 > node.value:
            return _lca(node.right, v1, v2)
        if v1 < node.value and v2 < node.value:
            return _lca(node.left, v1, v2)
        if node.value <= v2 and node.value >= v1:
            return node.value

    return _lca(tree, min(v1, v2), max(v1, v2))
    
def make_tree(vals):
    tree = None
    for val in vals:
        tree = insert(val, tree)
    return tree

    
#######################tests##############################
from numpy import random
def should_insert_values():
    for n in [50, 100, 500, 1000]:
        a = random.randint(1001, size=n)
        tree = make_tree(a)
        assert inorder(tree) == sorted(a)

def should_delete_nodes():
    for i in range(3):
        arr = sorted(random.randint(1000, size=10))
        tree = make_tree(arr)
        while len(arr) > 0:
            assert inorder(tree) == arr
            val = arr[random.randint(0, len(arr))]
            arr.remove(val)
            tree = delete(tree, val)
            if len(arr) > 1:
                assert tree
        assert not tree

def should_find_nth_element():
    for i in range(5):
        arr = random.randint(100, size=20)
        sorted_arr = sorted(arr)
        tree = make_tree(arr.tolist())
        for i in range(5):
            n = random.randint(low=1, high=20)
            assert nth_highest(tree, n) == sorted_arr[-n]

def should_find_lca():
    '''
        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   1       4       7       9
         /  \
         3   5
    
 lca(5,2)=2
 lca(1,5)=2
 lca(2,9)=6
'''
    tree = Node(6,
                Node(2,
                     Node(1),
                     Node(4,
                          Node(3),
                          Node(5))),
                Node(8,
                     Node(7),
                     Node(9)))
    assert 2 == lca(tree, 5, 2) 
    assert 2 == lca(tree, 1, 5) 
    assert 6 == lca(tree, 2, 9) 

    assert 1 == lca(Node(1, right=Node(2, right=Node(3))), 1, 3)
    assert 2 == lca(Node(2, Node(2), Node(3)), 1, 3)
    assert 3 == lca(Node(3, Node(2, Node(1))), 1, 3)

