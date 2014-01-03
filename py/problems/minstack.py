class Node:

    def __init__(self, value,  next, nextmin=None):
        self.value = value
        self.next = next
        self.nextmin = nextmin


class Stack:
    def __init__(self):
        self.top = None
        self.min = None

    #O(1)
    def push(self, value):
        self.top = Node(value, self.top)
        if not self.min or value <= self.min.value:
            self.top.nextmin = self.min
            self.min = self.top

    #O(1)
    def pop(self):
        if not self.top:
            return self.top
        node = self.top
        if node == self.min:
            self.min = self.min.nextmin
        self.top =  node.next
        return node.value

    #O(1)
    @property
    def min_val(self):
        return self.min.value if self.min else None
        

def should_work_for_duplciate_elements():
    s = Stack()
    assert not s.min_val
    s.push(5)
    assert 5 == s.min_val
    s.push(3)
    s.push(3)
    assert 3 == s.min_val
    s.push(10)
    assert 3 == s.min_val
    assert 10 == s.pop()
    assert 3 == s.min_val
    assert 3 == s.pop()
    assert 3 == s.min_val
    assert 3 == s.pop()
    assert 5 == s.min_val
    


import random

def random_numbers():
    a =  range(100)
    random.shuffle(a)
    return a
    
def should_work_for_random_data():
    a = random_numbers()
    s = Stack()
    for i in range(100):
        s.push(a[i])
        assert s.min_val == sorted(a[:i + 1])[0]
        
    for i in range(99,-1,-1):
        assert s.pop() == a[i]
        if i > 0:
            assert s.min_val ==  sorted(a[:i])[0]
    
    