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

    def is_leaf(self):
        return not(self.right or self.left)

    def __eq__(self, other):
        if not other:
            return False
        return (other.value == self.value and
                other.left == self.left and
                other.right == self.right)

    def __repr__(self):
        return "Node(%s%s%s)" % (self.value, ", left=" + repr(self.left)
                                 if self.left else "", ", right=" + repr(self.right)
                                 if self.right else "")
class buldymoulda_papasheeee:
    pass
        