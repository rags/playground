class SingleLinkNode(object):
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value) +  " -> " + str(self.next_node)
        
class DoubleLinkNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @property
    def prev(self):
        return self.left
        
    @property
    def next(self):
        return self.right
        
    @property
    def children(self):
        return self.left, self.right

    def other_child(self, child):
        return self.right if self.left is child else self.left

    @property
    def is_leaf(self):
        return not(self.right or self.left)

    def equivalent(self, other):
        if not other:
            return False
        if not self.left and other.left:
            return False
        if not self.right and other.right:
            return False
        if self.left and not self.left.equivalent(other.left):
            return False
        if self.right and not self.right.equivalent(other.right):
            return False
        return other.value == self.value

    def __repr__(self):
        return "Node(%s%s%s)" % (self.value, ", left=" + repr(self.left)
                                 if self.left else "", ", right=" + repr(self.right)
                                 if self.right else "")
class buldymoulda_papasheeee:
    pass
        