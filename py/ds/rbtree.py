    
from .nodes import DoubleLinkNode as Node
from .bst import  is_valid_binary_tree, next_descendant_in_order

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
    assert node.color == B


    parent = node.parent
    sibling = parent.other_child(node)
    assert sibling, strify(tree)
    nephew_left, nephew_right = sibling.children
    while node.color == B and (sibling.color == R or
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
                parent.right.color = B
         
        if sibling == parent.left:
            if nephew_right and not nephew_left:
                rotate_left(sibling)
                sibling = parent.other_child(node)
            rotate_right(parent)
            if sibling.left:
                sibling.left.color = B
            if parent.left:
                parent.left.color = B
        sibling.color = parent.color
        if parent.color == R:
            parent.color = B
            if parent.left:
                parent.left.color = R
            if parent.right:
                parent.right.color = R
        else:
            parent.color = R
            
        sibling = parent.other_child(node)
        if not sibling:
            detach_node(node)
            parent.color = B
            return find_root(tree)
        nephew_left, nephew_right = sibling.children
    if node.color == R:
        detach_node(node)
        return tree
    assert node.color == B

    if parent.color == R:
        detach_node(node)
        parent.color = B
        sibling.color = R
        return find_root(tree)
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
        nephew_left, nephew_right = sibling.children
        if (parent.color == B and nephew_left and nephew_right and
            R == nephew_right.color and R == nephew_left.color):
            sibling.color = R
            nephew_left.color = nephew_right.color = B
        #Sibling color is red - can fix locally
        if sibling.color == R:
            (rotate_left if sibling == parent.right else rotate_right)(parent)
            parent.color = R
            sibling.color = B
            sibling = parent.other_child(node)
            nephew_left, nephew_right = sibling.children
            assert sibling.color == B, strify(find_root(parent))
            
        # one of the sibling child is red. So sibling cant be colored red
        # rotate to make left and right back height equal and continue
        if ((nephew_left and nephew_left.color == R) or
            (nephew_right and nephew_right.color == R)):
            if sibling == parent.right:
                if nephew_left and not nephew_right:
                    rotate_right(sibling)
                    sibling = parent.right
                if nephew_right.color == B:
                    rotate_right(sibling)
                    nephew_left.color = B
                    sibling.color = R
                    sibling = parent.right

                rotate_left(parent)
                assert sibling.right
                if parent.color == B:
                    sibling.right.color = B
            else:
                if nephew_right and not nephew_left:
                    rotate_left(sibling)
                    sibling = parent.left
                if nephew_left.color == B:
                    rotate_left(sibling)
                    nephew_right.color = B
                    sibling.color = R
                    sibling = parent.left

                rotate_right(parent)
                assert sibling.left
                if parent.color == B:
                    sibling.left.color = B
            if parent.color == R and parent.parent.other_child(parent).color == R:
                parent.parent.color = R
                parent.parent.other_child(parent).color = parent.color =  B
                
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
    if tree.color == BB:
        print "unbalanced double balck node %s in tree %s" % (tree.value, strify(tree))
        return False, 0
        
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

def strify(node):
    valstr = ("<<%s>>" % node.value) if node.color == BB else ("[%s]" % node.value) if node.color == R else node.value 
    if not(node.left or node.right):
        return valstr
    return "(%s%s%s)" % (
        valstr,
        (", L=%s" % strify(node.left)) if node.left else '', 
        (", R=%s" % strify(node.right)) if node.right else '')
