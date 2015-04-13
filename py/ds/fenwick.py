def next(index):
    return index + lastBit(index)

def prev(index):
    return index - lastBit(index)

def lastBit(num):
    return num & -num 
        
# A tree with 1 based index
class Fenwick:

    def __init__(self, max):
        self.max = max
        self.tree = [None] * (max + 1)

    def create(arr):
        tree = Fenwick(len(arr))
        for i, val in enumerate(arr):
            tree.add(i + 1, val)
        return tree
            
    def add(self, index, value):
        assert self.isInRange(index), "index should between 1 and %d" % self.max
        self.tree[index] = (self.tree[index] + value) if self.tree[index] else value
        next_ = next(index)
        if self.isInRange(next_):
            self.add(next_, value)
                
    def isInRange(self, index):
        return index > 0 and index <= self.max
        
    def __getitem__(self, index):
        assert self.isInRange(index), "index should between 1 and %d" % self.max
        prev_ = prev(index)
        return self[prev_] + self.tree[index] if self.isInRange(prev_) else self.tree[index]
            

############################## TESTS ##############################

def should_update_tree():
    tree = Fenwick.create(list(range(1, 11)))
    tree.add(5, 5)
    assert tree[4] == 10
    assert tree[5] == 20
    assert tree[10] == 60
    
def should_create_tree():
    tree = Fenwick.create(list(range(1, 11)))
    assert tree[10] == 55
    assert tree[4] == 10
    assert tree[5] == 15
