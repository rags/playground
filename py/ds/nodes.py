class SingleLinkNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value) +  " -> " + str(self.next_node)
        
class DoubleLinkNode:
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
        