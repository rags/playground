from collections import namedtuple
Node = namedtuple('Node', ['val', 'left', 'right'], verbose=True)
Node.__new__.__defaults__ = (None, None)
operators = {'+','-', "/", '%', '*','//'}

def validate(node):
    return node is not None and type(node) is Node and ((node.val in operators and node.left is not None and node.right is not None and validate(node.left) and validate(node.right)) or (node.val not in operators and node.left is None and node.right is None))

#################### TESTS ####################
def should_validate_legit_node():
    assert validate(Node(1))
    assert validate(Node('+', Node(1), Node(2)))
    assert validate(Node('*',
                         Node('+', Node(1), Node(2)),
                         Node(3)))
    assert validate(Node('%',
                         Node('*', Node(1), Node(2)),
                         Node('/', Node(3), Node(4))))

def should_invalidate_bad_ombres():
    assert not validate(None)
    assert not validate(Node(1, Node(3)))
    assert not validate(Node(1, Node(3), Node(4)))
    assert not validate(Node('+'))
    assert not validate(Node('+', Node('-'), Node(4)))
