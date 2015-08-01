        
# A tree with 1 based index
class Fenwick1:

    def __init__(self, max, default=0):
        self.max = max
        self.tree = [default] * (max + 1)
        
    @classmethod
    def create(cls, arr, default=0):
        tree = Fenwick1(len(arr), default)
        for i, val in enumerate(arr):
            tree.add(i + 1, val)
        return tree
            
    def add(self, index, value):
        assert self.is_in_range(index), "index should between 1 and %d" % self.max
        self.tree[index] = (self.tree[index] + value) if self.tree[index] else value
        next_ = Fenwick1.next(index)
        if self.is_in_range(next_):
            self.add(next_, value)
                
    def is_in_range(self, index):
        return index > 0 and index <= self.max
        
    def __str__(self):
        return str(self.tree)

    def __repr__(self):
        return str(self)
            
    def __setitem__(self, index, value):
        self.add(index, value - (self[index] - self[index - 1]))
        
    def __getitem__(self, index):
        assert index == 0 or self.is_in_range(index), "index should between 0 and %d" % self.max
        prev_ = Fenwick1.prev(index)
        # print(index, prev_, self.is_in_range(prev_), self.tree[index])
        return self.tree[index] if not self.is_in_range(prev_) else (self[prev_] + self.tree[index])

    @staticmethod
    def next(index):
        return index + Fenwick1.lastBit(index)
        
    @staticmethod
    def prev(index):
        return index - Fenwick1.lastBit(index)
        
    @staticmethod
    def lastBit(num):
        return num & -num 
    
# A tree with 0 based index
class Fenwick:

    def __init__(self, max, default=0):
        self.max = max
        self.tree = [default] * max 
        self.default = default

    @classmethod
    def create(cls, arr, default=0):
        tree = Fenwick(len(arr), default)
        for i, val in enumerate(arr):
            tree.add(i, val)
        return tree
            
    def add(self, index, value):
        assert self.is_in_range(index), "index should be less than %d" % self.max
        self.tree[index] = (self.tree[index] + value) if self.tree[index] else value
        next_ = Fenwick.next(index)
        if self.is_in_range(next_):
            self.add(next_, value)
                
    def is_in_range(self, index):
        return index > -1 and index < self.max
        
    def __str__(self):
        return str(self.tree)

    def __repr__(self):
        return str(self)
            
    def __setitem__(self, index, value):
        self.add(index, value - (self[index] - self[index - 1]))
        
    def __getitem__(self, index):
        assert self.is_in_range(index), "index should less than %d" % self.max
        return self.get_item(index + 1)
        
    def get_item(self, n):
        sum = self.default
        while n > 0:
            sum += self.tree[n-1]
            n=Fenwick.prev(n)
        return sum

    @staticmethod
    def next(index):
        return index | index+1
        
    @staticmethod
    def prev(index):
        return index & index-1
    
        
############################## TESTS ##############################

import pytest
@pytest.mark.parametrize("BITreeImpl,i", [
    (Fenwick1,1),
    (Fenwick,0)
])	
def should_update_tree(BITreeImpl, i):
    tree = BITreeImpl.create(list(range(1, 11)))
    tree.add(4+i, 5)
    assert tree[3+i] == 10
    assert tree[4+i] == 20
    assert tree[9+i] == 60
    tree[4+i] = 5
    assert tree[4+i] == 15
    assert tree[9+i] == 55

@pytest.mark.parametrize("BITreeImpl,i", [
    (Fenwick1,1),
    (Fenwick,0)

])
def should_create_tree(BITreeImpl,i):
    tree = BITreeImpl.create(list(range(1, 11)))
    assert tree[9+i] == 55
    assert tree[3+i] == 10
    assert tree[4+i] == 15

@pytest.mark.parametrize("BITreeImpl,i", [
    (Fenwick1,1),
    (Fenwick,0)

])
def should_create_tree_from_scratch(BITreeImpl,i):
    tree = BITreeImpl(3)
    tree.add(0+i, 2)
    assert tree[0+i] == tree[i+i] == 2
    assert tree[2+i] == 2
