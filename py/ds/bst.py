from nodes import DoubleLinkNode as Node

def insert(value, tree=None):
    if not tree:
        return Node(value)
    node = _find(tree, value)[0]
    if node.value == value:
        return tree
    if node.value > value:
        node.left = Node(value)
    else:
        node.right = Node(value)
    return tree

def search(tree, value):
    node = _find(tree, value)[0]
    return node.value == value
        
def _find(node, value, parent=None):
    if not node:
        raise Exception("empty node")
    if node.value > value and node.left:
        return _find(node.left, value, node)
    if node.value < value and node.right:
        return _find(node.right, value, node)
    return (node, parent)

def _inorder(node, vals):
    if not node:
        return vals
    _inorder(node.left, vals)
    vals.append(node.value)
    _inorder(node.right, vals)
    
def inorder(tree):
    values = []
    _inorder(tree, values)
    return values

def left_most(node, parent):
    while(node.left):
        parent = node
        node = node.left
    return node, parent
    
def next_in_order(node):#left most child in the right branch of the node is the next number in sequence
    return left_most(node.right, node)
    
def delete(tree, value):
    node, parent= _find(tree, value)
    if node.value != value:
        return tree
    if not (node.right and node.left): # the node has either one or no children
        return delete_node_with_1_or_0_children(parent, node,
                                                node.right or node.left or None, tree)

    #node has both children
    next_node, next_node_parent = next_in_order(node)
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

    
def make_tree(vals):
    tree = None
    for val in vals:
        tree = insert(val, tree)
    return tree

#######################tests##############################
from arrays import array
import random
def should_insert_values():
    for n in [50, 100, 500, 1000]:
        a = array(n)
        tree = make_tree(a)
        assert inorder(tree) == sorted(a)

def should_delete_nodes():
    arr = range(100)
    tree = make_tree(arr)
    while len(arr) > 0:
        assert inorder(tree) == arr
        val = random.choice(arr)
        arr.remove(val)
        tree = delete(tree, val)
    assert tree
    assert not tree