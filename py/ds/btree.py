class Node(object):
    def __init__(self, k=3, values=None, children=None):
        self.k = k
        self.values = values or []
        self.children = children or []

    @property
    def is_valid(self):
        for child in self.children:
            if not child.is_valid:
                return False
        return (self.len <= self.k and
                sorted(self.values) == self.values and
                len(self.children) <= self.len + 1)

    @property
    def len(self):
        return len(self.values)

    @property
    def next_level_full(self):
        return (len(self.children) == self.k + 1 and
                all(child.is_full for child in self.children))
        
    @property
    def is_full(self):
        assert self.is_valid
        return self.len == self.k

    def find_pos_for(self, val):
        for i, ele in enumerate(self.values):
            if ele >= val:
                return i
        return self.len

    def insert_at(self, i, val, safe=True):
        if safe:
            assert self.len + 1 <= self.k
        self.values.insert(i, val)

    def _insert(self, val, left, right):
        i = self.find_pos_for(val)
        self.insert_at(i, val)
        assert left and right
        if self.has_child(i):
            self.children[i] =left
        else:
            self.children.insert(i, left)

        self.children.insert(i + 1, right)

    def rotate_left(self, child_pos):
        assert child_pos > 0 and child_pos < len(self.children)
        left_i = child_pos - 1
        child =  self.children[child_pos]
        left_sibling = self.children[left_i]
        left_sibling.values.append(self.values[left_i])
        if child.children:
            left_sibling.children.append(child.children.pop(0))
        self.values[left_i] = child.values.pop(0)
        
    def rotate_right(self, child_pos):
        assert child_pos > -1 and child_pos < len(self.children) - 1
        right_i = child_pos + 1
        child =  self.children[child_pos]
        right_sibling = self.children[right_i]
        if len(child.children) > len(child.values):
            right_sibling.children.insert(0, child.children.pop())
        right_sibling.values.insert(0, self.values[child_pos])
        self.values[child_pos] = child.values.pop()
        
    
    def has_child(self, i):
        return i < len(self.children)
        
    def inorder(self, vals):
        assert not len(self.children) > self.len + 1
        for i, e in enumerate(self.values):
            if i < len(self.children):
                self.children[i].inorder(vals)
            vals.append(e)
        if self.len < len(self.children):
            self.children[self.len].inorder(vals)

    def get_or_create_nearest_non_full_sibling_for(self, child_pos):
        print "range", range(1, max(len(self.children) - child_pos, child_pos) + 1)
        for i in range(1, max(len(self.children) - child_pos, child_pos) + 1):
            left_sibling = child_pos - i
            if left_sibling >= 0 and not self.children[left_sibling].is_full:
                return left_sibling
            right_sibling = child_pos + i
            #if right_sibling == len(self.children):
            #    self.children.append(Node(self.k))
            #    return right_sibling
            
            if (right_sibling < len(self.children) and
                not self.children[right_sibling].is_full):
                return right_sibling
        
            
    def __repr__(self):
        r = repr(self.values)
        if self.children:
            r += "->"
        for child in self.children:
            r += repr(child)
        return "(" +  r + ")" if self.children else r

    #-1 return value means unbalanced tree
    def depth(self):
        child_depth = None
        for child in self.children:
            if child_depth is None:
                child_depth = child.depth()
            elif child_depth != child.depth() or child_depth == -1:
                return -1
        return (child_depth or 0) + 1
        
class BTree(object):
    def __init__(self, k=3):
        assert k >= 2
        self.k = k
        self.root = Node(k)

    '''
    Valid tree:
    1. Elements in order
    2. Root should have 0 or atleast 2 children
    3. Completely balanced
    '''
    def is_valid(self):
        if not self.root:
            return True
        root_children = self.root.children
        if not len(root_children) == 1: #0 children or atleast 2 children
            return False
        elements =  self.inorder()
        if elements != sorted(elements):
            return False
        if self.root.depth() ==- 1:
            return False
        return True
    

    def inorder(self):
        x = []
        self.root.inorder(x)
        return x

    def _split(self, node, parent, val_to_insert):
        i = node.find_pos_for(val_to_insert)
        split = node.len // 2
        split_val = node.values[split]
        right_children = node.children[split + 1:]
        right_values = node.values[split + 1:]
        node.values = node.values[:split]
        node.children = node.children[:split + 1]
        right = (Node(self.k) if not (right_children or right_values) else
                 right_children[0] if (len(right_children) == 1 and
                                   not right_values)
                 else Node(node.k, right_values, right_children))
        
        print "left after split", node
        left = node
        
        if self.root == node:
            self.root = parent
            print "new_root", self.inorder()
        
        if i > node.len:
            print "old i %s" % i
            i -= (node.len + 1)
            print "new i %s" % i
            if not right:
                right = Node(self.k)
            return right
        
        parent._insert(split_val,left, right)
        
        print "r", self.root
        print ("A", parent.values, left.values if left else '<empty lf>',
               right.values if right else '<empty rt>', self.inorder())
        print '</end split>'
        return node

                

    def insert(self, val):
        node = self.root
        parent = None
        node_pos = None
        print self.root
        while True:
            if node.is_full:
               if parent and (node.next_level_full or not node.children):
                   assert node_pos is not None
                   print "pos for %s in %s is %s" % (val, node, node_pos)
                   sibling_i = parent.get_or_create_nearest_non_full_sibling_for(node_pos)
                   
                   if sibling_i is not None: #move element to the sibling

                       if not node.children: #leaf node
                           node.insert_at(node.find_pos_for(val), val, False)
                           if sibling_i < node_pos: #rotate left
                               for j in range(sibling_i + 1, node_pos + 1):
                                   parent.rotate_left(j)
                           else: #rotate right
                               for j in range(sibling_i - 1, node_pos - 1, -1):
                                   parent.rotate_right(j)
                           return #done inserting

                       print "found sibling %s for node at %s" %  (sibling_i, node_pos)
                       if sibling_i < node_pos: #rotate left
                           next = ((parent.children[node_pos - 1], node_pos - 1)
                                   if val <= node.values[0] else
                                   (node, node_pos))
                           for j in range(sibling_i + 1, node_pos + 1):
                               parent.rotate_left(j)
                       else: #rotate right
                           next = ((parent.children[node_pos + 1], node_pos + 1)
                                   if val > node.values[-1] else
                                   (node, node_pos))
                           for j in range(sibling_i - 1, node_pos - 1, -1):
                               parent.rotate_right(j)
                       print "After rotations parent = %s" %  parent
                       node, node_pos = next
                       print "After rotations node = " %  parent
                       continue        
                   else:
                       print "No sibling found for %s" %  node
                       assert not parent.is_full, node
                       if node.k == 2:# 2 way node need special logic to split
                           if not node.children: # leaf node
                               low, mid, high = sorted([val] + node.values)
                               print "LMH = ", low, mid, high
                               node.values = [high]
                               parent._insert(mid,Node(self.k, [low]), node)
                               return # done inserting
                           else:
                               child1, child2 = node.children.pop(0), node.children[0]
                               new_node = Node(self.k, [child1.values.pop()],
                                               [child1,
                                                Node(self.k, [node.values.pop(0)],
                                                 [child1.children.pop(),
                                                  child2.children.pop(0)]
                                                     if child1.children else [])])
                               val_to_promote = child2.values.pop(0)
                               parent._insert(val_to_promote,new_node, node)
                               node = new_node if val < val_to_promote else node
                       else:
                           node = self._split(node, parent, val)
                       print "Tree After split %s" % self.root
               elif not parent: #root node
                   if node.k == 2:# 2 way node need special logic to split
                       if not node.children:
                           left, root, right = sorted(node.values + [val])
                           node.values = [root]
                           node.children = [Node(node.k, [left]), Node(node.k, [right])]
                           return
                       if node.next_level_full:
                           val1, val2= node.values
                           child1, child2, child3 = node.children
                           if child1.children:
                               assert (self.k + 1 == len(child1.children)
                                       == len(child2.children) == len(child3.children))
                           right_left = Node(self.k, [val2],
                                             [child2.children.pop(), child3.children.pop(0)]
                                             if child2.children else [])
                           left, right = (Node(self.k, [val1], [child1, child2]),
                                          Node(self.k, [child3.values.pop(0)],
                                               [right_left, child3]))
                           node.values = [child2.values.pop()]
                           node.children = [left, right]
                  
                   else:
                       if not node.children or node.next_level_full:
                           parent = Node(node.k)
                           node = self._split(node, parent, val)
                    
            # Ensure you are inserting to leaf node thats not full
            i = node.find_pos_for(val)
            if node.has_child(i):
                parent, node = node, node.children[i]
                node_pos = i
                continue

            assert not node.is_full and len(node.children) <= i
            node.insert_at(i, val)
            print "inserted %s" % val, self.root
            return


################################### TESTS ###################################
from numpy import random

def should_insert():
    #eles = [32, 51, 15, 94, 54, 9, 63, 51, 62, 47, 76, 57, 45, 99, 88, 46, 96, 82, 89, 6, 93, 69, 12, 11, 62]
    eles = [8, 28, 57, 91, 90, 77, 61, 76, 5, 99, 75, 69, 28, 69, 64, 19, 98, 11, 9, 23, 16, 84, 72, 20, 60]
    for k in [2]:
            #range(2, 7):
            print "%s way btree" %  k
            tree = BTree(k)
            print eles
            for i, e in enumerate(eles, start=1):
                print "inserting %s" %  e
                tree.insert(e)
                print "After insert of %s" % e, tree.root
                print "Tree order", tree.inorder(), "sorted", sorted(eles[:i])
                assert tree.root.is_valid
                assert tree.inorder() == sorted(eles[:i])
            assert sorted(eles) == tree.inorder()

def should_insert1():
    for i in range(25):
        eles = random.randint(1, 100, size=25)
        for k in [2]:
            #range(2, 7):
            print "%s way btree" %  k
            tree = BTree(k)
            print eles
            for e in eles:
                print "inserting %s" %  e
                tree.insert(e)
                print tree.root
                print tree.inorder()
                assert tree.root.is_valid
            assert sorted(eles) == tree.inorder()


if __name__ == '__main__':
    should_insert()