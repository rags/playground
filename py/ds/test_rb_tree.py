
from rbtree import insert, make_node, delete, is_valid, B,  R,  strify,  swap_with_successor,  find,  rotate_right, rotate_left
from tree_ops import inorder
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
    for i in range(10):
        inputs = list(rand.randint(10000, size=3000))
        tree = reduce(lambda tree, val: insert(val, tree), inputs, None)
        assert is_valid(tree)
        assert inorder(tree) == sorted(inputs)
        for i in range(2500):
            val = inputs.pop()
#            print "delete %s from tree %s" %  (val, strify(tree))
            tree = delete(val, tree)
#            assert is_valid(tree), strify(tree)
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
    assert sample_tree().equivalent(tree)

    
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
    assert four.equivalent(four.left.parent)
    two = four.parent
    assert 2 == two.value
    assert not two.parent # 2 is root
    original_tree = sample_tree()
    assert inorder(original_tree) == inorder(two)
    rotate_left(two)
    assert four.equivalent(original_tree)
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
        print strify(tree)
        tree = delete(4, tree)
        print strify(tree)
        assert is_valid(tree)
        vals.remove(4)
        assert vals == inorder(tree)

def should_delete_with_dups():
    tree = N(3,
             N(1,N(1),N(2), R), 
             N(5,N(4),N(6,right=N(7, color=R)), R))
    assert is_valid(tree)
    tree = delete(1, tree)
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
    assert is_valid(tree)
    assert [1, 2, 3, 4] == inorder(tree)
