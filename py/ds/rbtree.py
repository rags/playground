    
from .nodes import DoubleLinkNode as Node
from .bst import  is_valid_binary_tree, next_descendant_in_order
from tree_ops import inorder

R, B, BB= 'R', 'B', '2B'

def make_node(data, parent=None, color=R, left=None, right=None):
    node = Node(data, left, right)
    node.color = color
    node.parent = parent
    return node
'''
To delete
1. ensure node to be deleted is leaf
2. Next if either node ot its parent is red,
   the deletion is simple-black height is not changed.
3. if both node and its parent are black.
   make parent red, by recoloring top down, push red down from nearest red ancestor
   make root red if necessary (in case these is no red ancestor) and trickle redness down
   goto step 2
'''
def delete(value, tree):
    node = find(value, tree)
    if not node:
        return tree
    if not node.parent and node.is_leaf:
        return None

    if not node.is_leaf:
        node = swap_with_successor(node)
    assert node.is_leaf
    if node.color == R:
        detach_node(node)
        return tree

    parent = node.parent
    assert node.color == B
    sibling = parent.other_child(node)
    assert sibling, strify(tree)
    nephew_left, nephew_right = sibling.children
    if (sibling.color == R or
        (nephew_left and nephew_left.color == R) or
        (nephew_right and nephew_right.color == R)):
        if sibling == parent.right:
            if nephew_left and not nephew_right:
                rotate_right(sibling)
                sibling = parent.other_child(node)
            rotate_left(parent)
            if sibling.right:
                sibling.right.color = B
            if parent.right:
                parent.right.color = R
        if sibling == parent.left:
            if nephew_right and not nephew_left:
                rotate_left(sibling)
                sibling = parent.other_child(node)
            rotate_right(parent)
            if sibling.left:
                sibling.left.color = B
            if parent.left:
                parent.left.color = R
            
        sibling.color = parent.color
        parent.color = B
        
        detach_node(node)
        return find_root(tree)
    if parent.color == R:
        detach_node(node)
        parent.color = B
        sibling.color = R
        return tree
    # black subtree - double-black
    assert parent.color == B and node.color == B and sibling.color == B
    assert not (sibling.left or sibling.right)
    detach_node(node)
    parent.color = BB
    sibling.color = R
    fix_double_black(parent)
    return find_root(tree)

def fix_double_black(node):
    while(node.color == BB):
        parent =  node.parent
        if not parent:
            node.color = B
            return
        sibling = parent.other_child(node)
        #Sibling color is red - can fix locally
        if sibling.color == R:

            (rotate_left if sibling == parent.right else rotate_right)(parent)
            node.color = parent.color = sibling.color = B
            sibling = parent.other_child(node)
            sibling.color = R
            return
        nephew_left, nephew_right = sibling.children
        # one of the sibling child is red. So sibling cant be colored red
        # rotate to make left and right back height equal and continue
        if ((nephew_left and nephew_left.color == R) or
            (nephew_right and nephew_right.color == R)):
            if sibling == parent.right:
                if nephew_left and not nephew_right:
                    rotate_right(sibling)
                rotate_left(parent)
            else:
                if nephew_right and not nephew_left:
                    rotate_left(sibling)
                rotate_right(parent)
            node.color = B
            return
            #node = sibling
            #node.color = BB
            #continue

        #sibling can be colored red
        sibling.color = R
        node.color = B
        if parent.color == R: 
            parent.color = B
            return
        else:
            node = parent
            node.color = BB
        
def make_red(node):
    path_up = []
    while node.parent and node.color!= R:
        path_up.append(node)
        node = node.parent
    while path_up:
        node.color = B
        if node.left:
            
            node.left.color = R
        if node.right:
            node.right.color = R
        node = path_up.pop()
    assert node.color == R
    return node
        
        
    
def detach_node(node):
    parent = node.parent
    if parent.left is node:
        parent.left = None
    else:
        parent.right = None
    node.parent = None
'''
 ensures that node to be deleted is a leaf node
       3
     /    \
    1      5
   /      /  \
 -2      4    6
 case 1: to delete 3 swap it with next item inorder, i.e 4.
 case 2: to delete 1 swap it with -2
 (1 does not have descendant sucessor, so swap with descendant predecessor)
Case 3:
    3                      4                  4               4        
  /   \                  /   \              /   \           /   \      
1      4          =>   1      3       =>  1      5    =>  1      5     
        \                      \                  X                   
         (5)                    (5)                (3)             
In this case to trickle down 3 to leaf is 2 step process
'''
def swap_with_successor(node):
    assert not node.is_leaf
    successor = next_descendant_in_order(node)[0]
    '''
          |
         node 
        /    \
       X     None
      Only in this case X is successor.
      Note that X must a leaf node(will result in unbalanced tree id X has children
      since node doesnt have right subtree)
    '''
    
    if not successor: #case 2
        successor = node.left
    assert successor
    node.value, successor.value = successor.value, node.value
    if not successor.is_leaf: #will recurse atmost once - case 3
        return swap_with_successor(successor)
    return successor #case 1
    
def find(value, node):
    if not node:
        return None
    if value == node.value:
        return node
    if value > node.value:
        return find(value, node.right)
    return find(value, node.left)

'''
  3 cases when you add a new node to rb tree.
    case 1:
        B1                B1                R1      
      /    \            /    \            /    \   
    R2       R3      R2       R3  =>    B2       B3  
    |                         |       
  | R |                     | R | 


    case 2: (gets simplified to case 3)
                                             rotate left         rotate right               
        
             B1              B1                       B1                 B1      
           /    \          /    \                  /    \              /    \   
         R2       B3  OR B2       R3     =>    | R4 |     B3   OR    B2     | R4 | 
          \                     /              /                               \ 
          | R4 |             | R4 |           R2                                R3    


    case 3: 
                                                       rotate right      rotate left
    
             B1                 B1                          B2                 B2         
           /    \            /    \                       /    \            /    \        
          R2      B  OR    B       R2      =>           R3      R1  OR   R1       R3     
        /                            \                           \       /      
     | R3 |                         | R3 |                        B     B
'''

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
    uncle = grand_parent.other_child(parent)
    
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
    if not tree.color == B:
        print "Root needs to be black"
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

    for child in [tree.left, tree.right]:
        if child and child.parent!= tree:
            print "%s does point to its parent %s" %  (child, tree)
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
    return assign_parents(make_node(2, color=B, left=make_node(1)))
    
def valid_trunk_2_children():
    return assign_parents(make_node(2, color=B, left=make_node(1), right = make_node(3)))

    
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

    tree = assign_parents(make_node(4, color = B,
                     left = make_node(2,
                                      left=make_node(1, color=B), 
                                      right=make_node(3, color=B)), 
                     right = make_node(6, color = B,
                                       left = make_node(5), 
                                       right = make_node(7))))
    assert is_valid(tree)
    tree.left.right.value = tree.value + 1
    assert not is_valid(tree)

    tree = assign_parents(make_node(8, color = B,
                     left = make_node(4,
                                      left=make_node(2, color=B, 
                                                 left = make_node(1, color=B),
                                                 right = make_node(3, color=B)), 
                                      right=make_node(6, color=B,
                                                  left = make_node(5, color=B),
                                                  right = make_node(7, color=B))), 
                     right = make_node(10, color = B,
                                       left = make_node(9, color = B), 
                                       right = make_node(11, color = B))))
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
    for i in range(100):
        inputs = list(rand.randint(100, size=10))
        tree = reduce(lambda tree, val: insert(val, tree), inputs, None)
        assert is_valid(tree)
        assert inorder(tree) == sorted(inputs)
        for i in range(8):
            val = inputs.pop()
            print "delete %s from tree %s" %  (val, strify(tree))
            tree = delete(val, tree)
            assert is_valid(tree), strify(tree)
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
        2             (6)
        |              |
      -----          -----
     /     \        /     \ 
   (1)     (3)     5       7    

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

def blackify(node):
    if not node:
        return None
    node.color = B
    blackify(node.left)
    blackify(node.right)
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
    
    
def should_delete_from_sample():
    '''
               4
               |
             -------
           /         \
        2             (6)
        |              |
      -----          -----
     /     \        /     \ 
   (1)     (3)     5       7    
    '''
    tree = delete(3, sample_tree())
    assert not find(3, tree)
    assert [1, 2, 4, 5, 6, 7] == inorder(tree)

    tree = delete(4, sample_tree())
    print inorder(tree, 'color')
    assert is_valid(tree)
    assert tree.value == 5
    assert not tree.right.left
    assert tree.right.color == B
    assert tree.right.right.color == R

    tree = delete(6, sample_tree())
    assert is_valid(tree)
    assert tree.right.color == B
    assert not tree.right.right
    assert tree.right.left.color == R
    assert [5, 7] == inorder(tree.right)

    tree = delete(5, blackify(sample_tree()))
    assert is_valid(tree)
    assert [1, 2, 3, 4, 6, 7] == inorder(tree)
    assert tree.left.color == R
    assert tree.right.color == B
    assert not tree.right.left
    assert tree.right.right.color == R


def strify(node):
    valstr = ("<<%s>>" % node.value) if node.color == BB else ("[%s]" % node.value) if node.color == R else node.value 
    if not(node.left or node.right):
        return valstr
    return "(%s%s%s)" % (
        valstr,
        (", L=%s" % strify(node.left)) if node.left else '', 
        (", R=%s" % strify(node.right)) if node.right else '')
    
def should_delete_double_black():
    '''
   delete 3
    2         2
   / \  =>   /
  1   3    (1)

                   8
                   |
               ---------
            /             \
          4                12
         |                  |
       ----                ----          
     /      \            /      \        
    2        6          10       14       
  /   \    /  \       /   \     /  \      
 1     3  5    7     9     11  13   15     
 
    
    '''
    tree1 = N(2, N(1), N(3))
    tree1 = delete(3, tree1)
    
    assert is_valid(tree1)
    assert [1, 2] == inorder(tree1)
    tree2 =N(8,
             N(4,
               N(2, N(1), N(3)),
               N(6, N(5), N(7))),
             N(12,
               N(10, N(9), N(11)),
               N(14, N(13), N(15))))
    for i in range(1, 16):
        print strify(tree2)
        assert is_valid(tree2)
        assert range(i, 16) == inorder(tree2)
        print "remove %s from %s" % (i, strify(tree2))
        tree2 = delete(i, tree2)
    assert not tree2
    
def N(val, left=None, right=None, color=B):
    node = make_node(val, left=left, right=right, color=color)
    if left:
        left.parent = node
    if right:
        right.parent = node
    return node
    
def should_delete_corner_cases():
    '''
 delete 4 in this tree

 Example 1:
    
      3                       3            
    /    \                  /     \         
   2     (5)       =>      2      (7)       
  /     /   \             /      /   \      
(1)    4     7          (1)     5     8     
            /  \              X   \  
         (6)    (8)          (4)  (6) 


 Example 2:
 sibling black with single red child.
 Rotate to romve zig zag (if any) and rotate left.
    
         3                            3                        3          
       /    \                       /    \                   /    \       
      2     (5)    rotate right    2     (5)     left       2     (6)     
     /     /   \      =>          /     /   \     =>       /     /   \    
   (1)    4     7               (1)    4     6           (1)    5     7   
               /                              \                X
            (6)                               (7)            (4)


  Ex 3:
  black node, black parent but one of sibling or sibling's children is red
    
                                         3 
                                         |                    
            3                          -------
        /       \                   /          \               
       1         5                 1             7                
    /    \    /     \    =>     /    \        /     \         
  1       2  4      (7)        1       2     5       8           
                   /  \                    X   \         
                  6    8                 (4)   (6)       


                                         3                              3               
                                         |                              |                 
            3                          -------                        -------           
        /       \                   /          \        =>         /          \         
       1         5                 1             5                1             6        
    /    \    /     \    =>     /    \        /    \           /    \        /     \     
  1       2  4       7        1       2      4       6        1       2     5       7       
                   /                                  \                   X             
                 (6)                                  (7)               (4)             

    
    '''
    for tree in [
    make_node(3, color=B,
              left=make_node(2, color=B, left=make_node(1)), 
              right = make_node(5,
                                left=make_node(4, color=B),
                                right = make_node(7, color=B,
                                                  left=make_node(6),
                                                  right = make_node(8)))), 

    make_node(3, color=B,
              left=make_node(1, color=B, left=make_node(1)), 
              right = make_node(5,
                                left=make_node(4, color=B),
                                right = make_node(7, color=B, left=make_node(6)))), 
    make_node(3, color=B,
              left=make_node(1, color=B,                                     
                             left=make_node(1, color=B),
                             right = make_node(2, color =B)), 
              right = make_node(5, color=B, 
                                left=make_node(4, color=B),
                                right = make_node(7, color=B,
                                                  left=make_node(6),
                                                  right = make_node(8)))), 
    make_node(3, color=B,
              left=make_node(1, color=B,                                     
                             left=make_node(1, color=B),
                             right = make_node(2, color =B)), 
              right = make_node(5, color=B, 
                                left=make_node(4, color=B),
                                right = make_node(7, color=B,
                                                  left=make_node(6))))]:
        tree = assign_parents(tree)
        assert is_valid(tree) # ensure test data is valid
        vals =  inorder(tree)
        tree = delete(4, tree)
        assert is_valid(tree)
        vals.remove(4)
        assert vals == inorder(tree)

def should_delete_with_dups():
    tree = N(3,
             N(1,N(1),N(2), R), 
             N(5,N(4),N(6,right=N(7, color=R)), R))
    assert is_valid(tree)
    tree = delete(1, tree)
    print strify(tree)
    assert is_valid(tree)
    assert [1, 2, 3, 4, 5, 6, 7] == inorder(tree)

def should_swap_with_successor_dups():
    tree = N(1, N(1), N(2))
    node = swap_with_successor(tree)
    assert node == tree.right
    assert node.value == 1
    assert node.parent.value== 2
    assert node.parent.left.value == 1

def should_delete_node_with_red_sibling():
    tree = N(4, N(2, N(1), N(3), R), N(5))
    assert is_valid(tree)
    tree = delete(5, tree)
    print strify(tree)
    assert is_valid(tree)
    assert [1, 2, 3, 4] == inorder(tree)
