from __future__ import division
def Var(i):
    return Leaf(i, 'Var')
def Val(i):
    return Leaf(i, 'Val')

class Leaf(object):
    def __init__(self, weight, type):
        self.type = type
        self.weight = weight
    def __repr__(self):
        return str(self)
    def __str__(self):
        return str(self.weight) + ('x' if self.type == "Var" else '')
    def mult(self, other):
        self.weight *= other.weight
        assert not (self.type == 'Var' and other.type == 'Var')
        self.type = 'Var' if self.type == 'Var' or other.type == 'Var' else self.type
    def eq(self, other):
        if not isinstance(other, Leaf):
            return False
        return self.weight == other.weight and self.type == other.type
        
class Binary(object):
    def __init__(self, value, left,  right):
        self.value = value
        self.left = left
        self.right = right
        
    def eq(self, other):
        return (self.value == other.value and
                other.left.eq(self.left) and other.right.eq(self.right))

    def __str__(self):
        return '(%s %s %s)' % (self.value, self.left, self.right)


class Minus(object):
    def __init__(self, child):
        self.child = child
        
    def eq(self, other):
        if not isinstance(other, Minus):
            return False
        return other.child.eq(self.child)
    def __str__(self):
        return '(- %s)' % str(self.child)
        
        
def solve(eqn):
    print (build_tree(tokenize(eqn)))
    tree = removeminus(remove_mult(build_tree(tokenize(eqn))))
    print tree
    vars, vals = [], []
    if isinstance(tree, Binary) and tree.value == "=":
        collect(tree.left, vars, vals)
        right_vars, right_vals = [], []
        collect(tree.right, right_vars, right_vals)
        vars.extend(map(int.__neg__, right_vars))
        vals.extend(map(int.__neg__, right_vals))
    else:
        collect(tree, vars, vals)
    denom = sum(vars)
    return (- sum(vals) / denom) if denom else 0
        

def collect(node, vars, vals):
    if isinstance(node, Binary):
        collect(node.left, vars, vals)
        collect(node.right, vars, vals)
    elif node.type == 'Var':
        vars.append(node.weight)
    else:
        vals.append(node.weight)
        

def make_exp(vars, ops):
    op = ops.pop()
    r= vars.pop()
    if op == 'Un' or (op == '-' and not vars):
        vars.append(Minus(r))
        return
    l = vars.pop()
    vars.append(Binary(op, l, r))

def build_tree(tokens):
    i = 0
    vars = []
    ops = []
    while i < len(tokens):
        if isinstance(tokens[i], Leaf):
           vars.append(tokens[i])
        elif tokens[i] == '(':
            if i > 0 and (isinstance(tokens[i - 1], Leaf)):
                ops.append('*')
            ops.append('(')
        elif tokens[i] == '*':
            while ops and ops[-1] == 'Un':
                make_exp(vars, ops)
            ops.append(tokens[i])
        elif tokens[i] == '-' and (i == 0 or tokens[i - 1] == '(' or tokens[i - 1] == '='
                                   or tokens[i - 1] == '*' or tokens[i - 1] == '-'
                                   or tokens[i - 1] == '+'):
            ops.append('Un')
        elif tokens[i] in '+-':            
            while ops and (ops[-1] == '*' or ops[-1] == 'Un'):
                make_exp(vars, ops)
            ops.append(tokens[i])
        elif tokens[i] == ')':
            while ops[-1] != '(':
                make_exp(vars, ops)
            ops.pop()
        elif tokens[i] == '=':
            while ops and ops[-1] != '(':
                make_exp(vars, ops)
            ops.append('=')
        i += 1
    while ops:
        make_exp(vars, ops)
    return vars[0]
            
        
def tokenize(eqn):
    tokens = []
    i = 0
    while i < len(eqn):
        if eqn[i] in '()+-*=':
            tokens.append(eqn[i])
            i += 1
            continue
        buffer = ''
        while i < len(eqn) and eqn[i] in '0123456789x':
            buffer += eqn[i]
            i += 1
        if buffer:
            if 'x' in buffer:
                tokens.append(Leaf(int(buffer[:-1] or 1), 'Var'))
            else:
                tokens.append(Leaf(int(buffer), 'Val'))
            continue
        i += 1 #ignore all other chars
    return tokens

def multiply(node, multiplier):
    if isinstance(node, Leaf):
        node.mult(multiplier)
    if isinstance(node, Binary):
        multiply(node.left, multiplier)
        multiply(node.right, multiplier)
    if isinstance(node, Minus):
        multiply(node.child, multiplier)
        
def remove_mult(tree):
    return _remove_mult(tree, tree)
    
def _remove_mult(tree, node, parent=None):
    if isinstance(node, Minus):
        _remove_mult(tree, node.child, node)
    if isinstance(node, Binary):
        _remove_mult(tree, node.left, node)
        _remove_mult(tree, node.right, node)
        if node.value == '*':

            assert (isinstance(node.left, Leaf) or
                    isinstance(node.right, Leaf))
            if isinstance(node.left, Leaf):
                multiply(node.right, node.left)
                if parent:
                    remove_middle_node(parent, node, node.right)
                else:
                    return node.right
                    
            else:
                multiply(node.left, node.right)
                if parent:
                    remove_middle_node(parent, node, node.left)
                else:
                    return node.left

    return tree
                    
def toggle_sign(node, parent):
    if isinstance(node, Minus):
        toggle_sign(node.child, node)
        remove_middle_node(parent, node, node.child)
    elif isinstance(node, Binary):
        toggle_sign(node.left, node)
        if node.value == '-':
            node.value = '+'
        else:
            toggle_sign(node.right, node)
    else:
        node.weight = -node.weight
        
def remove_middle_node(grandpa, parent, child):
    if isinstance(grandpa, Minus):
            grandpa.child = child
    else:
        if parent == grandpa.left:
            grandpa.left = child
        else:
            grandpa.right = child

def removeminus(tree):
    return remove_minus(tree, tree)
    
def remove_minus(tree, node, parent=None):
    if isinstance(node, Binary):
        remove_minus(tree, node.left, node)
        if node.value == '-':
            node.value = '+'
            toggle_sign(node.right, node)
        else:
            remove_minus(tree, node.right, node)
    if isinstance(node, Minus):
        remove_minus(tree, node.child, node)
        toggle_sign(node.child, node)
        if not parent:
            return node.child
        else:
            remove_middle_node(parent, node, node.child)
    return tree
    

############################## TESTS ##############################


def assert_array_eq(arr1, arr2):
    assert len(arr1) == len(arr2)
    for i in range(len(arr1)):
        if isinstance(arr1[i], Leaf):
            assert arr1[i].eq(arr2[i])
        else:
            assert arr1[i] == arr2[i]
        
def should_build_tree():
    assert Binary('=', Binary('-', Var(1), Val(3)), Val(0)).eq(
              build_tree([Var(1), '-', Val(3), '=', Val(0)]))
    assert Binary('=', Binary('+', Var(1), Val(3)), Val(0)).eq(build_tree(tokenize('(x+3=0)')))
    assert Binary('=', Binary('+', Var(3), Val(3)), Var(1)).eq(
        build_tree(tokenize('(3x+3=x)')))

    assert Binary('=', Binary('*', Val(2), Binary('+', Var(1), Val(1))), Val(10)).eq(
                build_tree(tokenize('2(x + 1)=10')))
    assert Binary('=',
                  Binary('*', Val(3),
                              Binary('-', Var(1), Binary('+', Val(2), Var(1)))),
                  Var(1)).eq(build_tree(tokenize('3(x-(2+x))=x')))
    assert Binary('=',
                  Binary('+',
                         Var(2), 
                         Binary('-', Val(5), 
                                Binary('-', Var(3), Val(2)))),
                  Binary('+', Var(1), Val(5))).eq(build_tree(tokenize('(2x+ 5- (3x-2)=x+ 5)')))
    assert Binary('=',
                  Minus(Binary('+', Var(2), Binary('-', Val(5), Binary('-', Var(3), Val(2))))),
                  Binary('+', Var(1), Val(5))).eq(build_tree(tokenize('-(2x+ 5- (3x-2))=x+ 5')))

def should_remove_mults():
    assert Binary('-', Var(3), Binary('+', Val(6), Var(3))).eq(
        remove_mult(Binary('*', Val(3),
                           Binary('-', Var(1), Binary('+', Val(2), Var(1))))))
    assert Var(9).eq(remove_mult(Binary('*', Val(3), Var(3))))
    assert Var(9).eq(remove_mult(Binary('*', Var(3), Val(3))))
    assert Binary('-', Val(3), Var(9)).eq(remove_mult(Binary('*', Val(3), Binary('-', Val(1), Var(3)))))
    assert remove_mult(Minus(Val(3))).eq(Minus(Val(3)))
    
def should_remove_minus():
    assert Val(-3).eq(removeminus(Minus(Val(3))))
    assert Binary('+', Var(-2), Binary('+', Val(-5), Binary('+', Var(3), Val(-2)))).eq(removeminus(Minus(Binary('+', Var(2), Binary('-', Val(5), Binary('-', Var(3), Val(2)))))))
    
def should_tokenize():
    assert_array_eq([Var(1), '-', Val(3), '=', Val(0)], tokenize('x-3=0'))
    assert_array_eq(['(', Var(1), '+', Val(3), '=', Val(0), ')'], tokenize('(x+3=0)'))
    assert_array_eq(['(', Var(3), '+', Val(3), '=', Var(1), ')'], tokenize('(3x+3=x)'))
    assert_array_eq([Val(3), '(', Var(1), '-', '(', Val(2), '+', Var(1), ')', ')', '=', Var(1)], tokenize('3(x-(2+x))=x'))
    assert_array_eq(['(', Var(2), '+', Val(5), '-', '(', Var(3), '-', Val(2),
             ')', '=', Var(1), '+', Val(5), ')'], tokenize('(2x+ 5- (3x-2)=x+ 5)'))
    assert_array_eq(['-', '(', Var(2), '+', Val(5), '-', '(', Var(3), '-', Val(2), ')', ')',
             '=', Var(1), '+', Val(5)], tokenize('-(2x+ 5- (3x-2)) = x + 5'))
    assert_array_eq(['-', Val(2), '(', Var(1), '+', Val(1), ')', '=', '-', '(',
                     Val(20), '-', Val(10), ')'], tokenize('-2(x + 1)=-(20-10)'))
    
def should_solve():
    assert 3 == solve('x-3')
    assert 7 == solve('x+17=20+4')
    assert -3 == solve('x+3=0')
    assert 1 == solve('-(2x+ 5- (3x-2) = x + 5)')
    assert 1 == solve('-(2x+ 5- (3x-2) = x + 5)')
    assert 2 / 3 == solve('3x-2')
    assert 4 == solve('2x + 3=11')
    assert 4 == solve('2(x + 1)=10')
    assert 9 == solve('-2(x + 1=10)')
    assert 4 == solve('-2(x + 1)=-(20-10)')
    assert -9 == solve('2x + 5 - 6 = -17 - 2')
    assert -9 == solve('2x + 5 - 5 = -9 * 2')
