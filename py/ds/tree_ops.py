
def _inorder(node, vals, attr=None):
    if not node:
        return vals
    _inorder(node.left, vals, attr)
    vals.append(node.value if not attr else node.__getattribute__(attr))
    _inorder(node.right, vals, attr)
    
def inorder(tree, attr=None):
    values = []
    _inorder(tree, values, attr)
    return values

def rotate_left(pivot):
    right_child =  pivot.right
    if not right_child:
        return
    left_child = pivot.left
    pivot.value, right_child.value = right_child.value, pivot.value
    pivot.right = right_child.right
    pivot.left = right_child
    right_child.right = right_child.left
    right_child.left = left_child
    
    
def rotate_right(pivot):
    left_child =  pivot.left
    if not left_child:
        return
    right_child = pivot.right
    pivot.value, left_child.value = left_child.value, pivot.value
    pivot.left = left_child.left
    pivot.right = left_child
    left_child.left = left_child.right
    left_child.right = right_child

# lca for non-BST binary trees
def lca(tree, val1, val2):
    def _lca(node):
        val1_ans = node if node.value == val1 else None
        val2_ans = node if node.value == val2 else None
            
        for child in [node.right, node.left]:
            if not child:
                continue
            val1_ans_tmp, val2_ans_tmp = _lca(child)
            val1_ans = val1_ans or val1_ans_tmp
            val2_ans = val2_ans or val2_ans_tmp
            if val1_ans and val2_ans:
                return (val1_ans, val2_ans) if val1_ans == val2_ans else (node, node)
        return val1_ans, val2_ans
    return _lca(tree)[0].value

from collections import deque
    
DFS, BFS = 1, 2

def _traverse(lst, remove_method, res):
    while(lst):
        item = remove_method(lst)
        if item.left:
            lst.append(item.left)
        if item.right:
            lst.append(item.right)
        res.append(item.value)
    
    
def traverse(tree, method=DFS):
    res = []
    (_traverse([tree], list.pop, res) if method == DFS
     else _traverse(deque([tree]), deque.popleft, res))
    return res

######################################## TESTS ########################################

from nodes import DoubleLinkNode as Node

def tree_for_rotation():
    '''
    Tree for rotation - the pivot is 4
    
                   8
                 /
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
    return Node(8,
                Node(4,
                     Node(2, Node(1), Node(3)),
                     Node(6, Node(5), Node(7))))

def should_rotate_left():
    '''
    
                                                        8
                   8                                  /
                 /                                  6
               4                                    |
               |                    =>            -------
             -------                            /         \
           /         \                        4            7
        2              6                    /   \
        |              |                   2     5          
      -----          -----                 |         
     /     \        /     \              -----       
   1        3      5       7            /     \      
                                       1        3     

    '''
    tree = tree_for_rotation()
    before_inorder = inorder(tree)
    rotate_left(tree.left)
    assert before_inorder == inorder(tree)
    assert 6 == tree.left.value
    assert [7] == inorder(tree.left.right)
    assert 4 == tree.left.left.value
    assert [5] == inorder(tree.left.left.right)
    assert [1, 2, 3] == inorder(tree.left.left.left)

    rotate_right(tree.left)
    assert tree_for_rotation().equivalent(tree)

def should_rotate_right():
    '''
                   8                                      8             
                 /                                      /               
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
    tree = tree_for_rotation()
    rotate_right(tree.left)
    assert tree.equivalent(Node(8,
                        Node(2,
                             Node(1),
                             Node(4,
                                  Node(3),
                                  Node(6, Node(5), Node(7))))))
    assert [1, 2, 3, 4, 5, 6, 7, 8] == inorder(tree)
    rotate_left(tree.left)
    assert tree.equivalent(tree_for_rotation())


def should_rotate():
    '''
       3             2           1
      /    <=      /   \   <=     \
    2      =>    1       3  =>     2
   /                                 \
  1                                   3

'''

    #clockwise
    tree = Node(3, Node(2, Node(1)))
    rotate_left(tree)
    assert tree.equivalent(Node(3, Node(2, Node(1)))) #no change
    rotate_right(tree)
    assert tree.equivalent(Node(2, Node(1), Node(3)))
    rotate_right(tree)
    assert tree.equivalent(Node(1, right=Node(2, right=Node(3))))
    rotate_right(tree)
    assert tree.equivalent(Node(1, right=Node(2, right=Node(3)))) #no change

    #anti-clockwise
    rotate_left(tree)
    assert tree.equivalent(Node(2, Node(1), Node(3)))
    rotate_left(tree)
    assert tree.equivalent(Node(3, Node(2, Node(1))))
    
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
    assert 2 == lca(Node(2, Node(1), Node(3)), 1, 3)
    assert 3 == lca(Node(3, Node(2, Node(1))), 1, 3)

def should_traverse():
    assert [8, 4, 2, 6, 1, 3, 5, 7] == traverse(tree_for_rotation(), BFS)
    assert [8, 4, 6, 7, 5, 2, 3, 1] == traverse(tree_for_rotation(), DFS)
    tree = Node(6, #tree from should_find_lca()
                Node(2,
                     Node(1),
                     Node(4,
                          Node(3),
                          Node(5))),
                Node(8,
                     Node(7),
                     Node(9)))
    assert [6,2, 8, 1, 4, 7, 9, 3, 5] == traverse(tree, BFS)
    assert [6, 8, 9, 7, 2, 4, 5, 3, 1] == traverse(tree, DFS)
    assert [1, 2, 3] == traverse(Node(1, Node(2, Node(3))), BFS)
    assert [1, 2, 3] == traverse(Node(1, Node(2, Node(3))), DFS)
    '''
                    5
                  /   \
                4       6
              /          \
            3              7
          /                  \
        2                      8
      /                         \
    1                             9
    '''
    tree = Node(5,
                Node(4, Node(3, Node(2, Node(1)))),
                Node(6, right=Node(7, right=Node(8, right=Node(9)))))
    assert [5, 4, 6, 3, 7, 2, 8, 1, 9] == traverse(tree, BFS)
    assert [5, 6, 7, 8, 9, 4, 3, 2, 1] == traverse(tree, DFS)
 
