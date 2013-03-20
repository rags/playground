# 3 cases when you add a new node to rb tree.
#    case 1:
#        B1                B1                R1      
#      /    \            /    \            /    \   
#    R2       R3      R2       R3  =>    B2       B3  
#    |                         |       
#  | R |                     | R | 
#
#
#    case 2: (gets simplified to case 3)
#                                             rotate left         rotate right               
#        
#             B1              B1                       B1                 B1      
#           /    \          /    \                  /    \              /    \   
#         R2       B3  OR B2       R3     =>    | R4 |     B3   OR    B2     | R4 | 
#          \                     /              /                               \ 
#          | R4 |             | R4 |           R2                                R3    
#
#
#    case 3: 
#                                                       rotate right      rotate left
#    
#             B1                 B1                          B2                 B2         
#           /    \            /    \                       /    \            /    \        
#          R2      B  OR    B       R2      =>           R3      R1  OR   R1       R3     
#        /                            \                           \       /      
#     | R3 |                         | R3 |                        B     B

    
from .nodes import DoubleLinkNode as Node
from .bst import  is_valid_binary_tree
from tree_ops import inorder

R, B= 'R', 'B'

def make_node(data, parent=None, color=R, left=None, right=None):
    node = Node(data, left, right)
    node.color = color
    node.parent = parent
    return node

def insert(value, tree=None):
    if not tree:
        return make_node(value, color=B)

    parent = find_parent_for(value, tree)
    new_node = make_node(value, parent)
    if parent.value > value:
        parent.left = new_node
    else:
        parent.right = new_node
    return rebalance(tree, new_node)

def find_parent_for(value, node):
    if value < node.value:
        if not node.left:
            return node
        return find_parent_for(value, node.left)
    if node.right:
        return find_parent_for(value, node.right)
    return node

    
def rebalance(tree, node):
    parent = node.parent
    if not parent: # root node
        node.color = B
        return tree
    # This also takes care of case where node is immed child of root
    if parent.color == B: 
        return tree

    #red parent
    grand_parent = parent.parent
    assert grand_parent #at this point tree should have depth=2
    uncle = grand_parent.left if grand_parent.right == parent else grand_parent.right
    
    #red uncle,parent re-color - case 1
    if uncle and uncle.color == R:
        grand_parent.color = R
        parent.color = uncle.color = B
        return rebalance(tree, grand_parent)

    #red parent, black/no uncle - cant recolor, restructure instead

    #The following 2 cases ensure that newnode<-parent<-grandparent and in a straight line.
    #i.e restructure zig-zag (case 2)
    if node == parent.right and  parent == grand_parent.left:
        rotate_left(parent)
        return rebalance(tree, parent)
    if node == parent.left and  parent == grand_parent.right:
        rotate_right(parent)
        return rebalance(tree, parent)
        
    #grand_parent -> parent -> child in same line (case 3)

    if node == parent.left and parent == grand_parent.left:
        rotate_right(grand_parent)
    else:
        rotate_left(grand_parent)
    parent.color = B
    node.color = grand_parent.color = R
    return find_root(tree)

def find_root(node):
    while(node.parent):
        node = node.parent
    return node
    
    
    
    
def rotate_right(pivot):
    parent = pivot.parent
    left_child = pivot.left
    if not left_child:
        return
    if parent:
        if pivot == parent.left:
            parent.left = left_child
        else:
            parent.right = left_child

    lefts_right_child = left_child.right
    pivot.left = lefts_right_child
    left_child.right = pivot
    
    left_child.parent = parent
    if lefts_right_child:
        lefts_right_child.parent = pivot
    pivot.parent = left_child

def rotate_left(pivot):
    parent = pivot.parent
    right_child = pivot.right
    if not right_child:
        return
    if parent:
        if pivot == parent.left:
            parent.left = right_child
        else:
            parent.right = right_child

    rights_left_child = right_child.left
    pivot.right = rights_left_child
    right_child.left = pivot
    
    right_child.parent = parent
    if rights_left_child:
        rights_left_child.parent = pivot
    pivot.parent = right_child

    

def is_valid(tree):
    if not is_valid_binary_tree(tree):
        print "not a valid binary tree"
        return False
    return satisfies_rb_invariants(tree)[0] 
    
def satisfies_rb_invariants(tree):
    if not tree:
        return True, 0
        
    if tree.color == R and ((tree.left and tree.left.color == R) or
                              (tree.right and tree.right.color == R)):
        print("Red node %s has red children in one or more of %s, %s" %
              (tree.value,
               tree.left.value if tree.left else None,
               tree.right.value if tree.right else None))
        return False, 0

    left_valid, black_height_left= satisfies_rb_invariants(tree.left)
    right_valid, black_height_right= satisfies_rb_invariants(tree.right)
    if not(left_valid and right_valid):
        return False, 0

    if black_height_left != black_height_right:
        print("Black heights for %s dont match left=%s, right=%s" %
              (tree.value, black_height_left, black_height_right))
        return False, 0

    return True, ((black_height_left + 1)
                  if tree.color == B else black_height_left)
            
############################## TESTS ##############################
from numpy import random as rand

def valid_trunk_1_child():
    return make_node(2, color=B, left=make_node(1))
    
def valid_trunk_2_children():
    return make_node(2, color=B, left=make_node(1), right = make_node(3))

    
def should_satisfy_invariant():
    assert is_valid(valid_trunk_2_children())
    assert is_valid(valid_trunk_1_child())

    tree = valid_trunk_2_children()
    tree.left.left = make_node(-1, R)
    assert not is_valid(tree)
    tree.left.left = make_node(-1, B)
    
    tree = valid_trunk_2_children()
    tree.left.value = tree.value + 1
    assert not is_valid(tree)

    tree = valid_trunk_2_children()
    tree.right.value = tree.value - 1
    assert not is_valid(tree)

    tree = make_node(4, color = B,
                     left = make_node(2,
                                      left=make_node(1, color=B), 
                                      right=make_node(3, color=B)), 
                     right = make_node(6, color = B,
                                       left = make_node(5), 
                                       right = make_node(7)))
    assert is_valid(tree)
    tree.left.right.value = tree.value + 1
    assert not is_valid(tree)

    tree = make_node(8, color = B,
                     left = make_node(4,
                                      left=make_node(2, color=B, 
                                                 left = make_node(1, color=B),
                                                 right = make_node(3, color=B)), 
                                      right=make_node(6, color=B,
                                                  left = make_node(5, color=B),
                                                  right = make_node(7, color=B))), 
                     right = make_node(10, color = B,
                                       left = make_node(9, color = B), 
                                       right = make_node(11, color = B)))
    assert is_valid(tree)
    
def should_insert_inorder():
    for i in range(5):
        inputs = list(rand.randint(100, size=35))
        print inputs
        tree = None
        for j, val in enumerate(inputs):
            tree = insert(val, tree)
            values_in_order = inorder(tree)
            assert j + 1 == len(values_in_order)
            assert sorted(inputs[0: len(values_in_order)]) == values_in_order
            assert is_valid(tree)
        assert sorted(inputs) == inorder(tree)

def should_work_for_a_large_tree():
    for i in range(3):
        inputs = rand.randint(10000, size=3000)
        tree = reduce(lambda tree, val: insert(val, tree), inputs, None)
        assert is_valid(tree)
        assert inorder(tree) == sorted(inputs)
        
#not a valid rb tree
def sample_tree():
    '''
    Tree for rotation - the pivot is 4

               4
               |
             -------
           /         \
        2              6
        |              |
      -----          -----
     /     \        /     \ 
   1        3      5       7    

    '''
    return  assign_parents(make_node(4,color=B, 
                                     left = make_node(2, color=B,
                                                      left=make_node(1),
                                                      right = make_node(3)),
                                     right = make_node(6,
                                                       left=make_node(5, color=B),
                                                       right=make_node(7, color=B))))

def assign_parents(node):
    if not node:
        return node
    for child in [node.right, node.left]:
        if child:
            child.parent = node
            assign_parents(child)
    return node

def should_rotate_left():
    '''
    
                                         
                                         
                                                                         
               4                                          4              
               |                    =>                    |              
             -------                                    -------          
           /         \                                /         \        
        2              6                           3              6      
        |              |                          /               |      
      -----          -----                       2              -----    
     /     \        /     \                     /             /     \   
   1        3      5       7                  1              5       7  
                                        

    '''
    tree = sample_tree()
    before_inorder = inorder(tree)
    rotate_left(tree.left)
    assert before_inorder == inorder(tree)
    assert 3 == tree.left.value
    assert 2 == tree.left.left.value
    assert 1 == tree.left.left.left.value
    rotate_right(tree.left)
    assert sample_tree() == tree

    
def should_rotate_right():
    '''
    
    
               4                                      2                 
               |                    =>                |                 
             -------                                -------             
           /         \                            /         \               
        2              6                        1            4
        |              |                                   /   \
      -----          -----                                3     6         
     /     \        /     \                                     |         
   1        3      5       7                                   -----       
                                                              /     \      
                                                             5       7

    '''
    four = sample_tree()
    rotate_right(four)
    assert [3, 4, 5, 6, 7] == inorder(four)
    assert 3 == four.left.value
    assert four == four.left.parent
    two = four.parent
    assert 2 == two.value
    assert not two.parent # 2 is root
    original_tree = sample_tree()
    assert inorder(original_tree) == inorder(two)
    rotate_left(two)
    assert four == original_tree
    assert not four.parent # 4 is root again
    assert 2 == four.left.value
    assert 6 == four.right.value

    three = four.left.right
    assert 3 == three.value
    assert 2 == three.parent.value
    assert 4 == three.parent.parent.value
    
    
