from ds.nodes import SingleLinkNode as Node

class Tree:
    def __init__(self, value, cur_root = None):
        new_node = Node(value)
        if cur_root:
            new_node.next_node = cur_root.root
            self.len = cur_root.len +  1
        else:
            self.len = 1
        self.root = new_node
        
    def __cmp__(self, other):
        return self.len.__cmp__(other.len)

    def __iter__(self):
        node = self.root
        while node is not None:
            yield node.value
            node = node.next_node
            
    def __str__(self):
        return str(self.root)
            
def non_decreasing_seq(seq):
    if not seq:
        return []
    subseqs = [Tree(seq[0])]
    for i in range(1, len(seq)):
        cur = seq[i]
        match = None
        for j in range(len(subseqs)):
            if subseqs[j].root.value <= cur:
                if not match or subseqs[j].len > match.len:
                    match = subseqs[j] 
       
        subseqs.append(Tree(cur, match))
    return max(subseqs)


from intro_to_algos.sort.arrays import array
from longest_inc_sub_seq_brute import non_decreasing_seq_brute

def assert_correct_length(arr):
    seq = non_decreasing_seq(arr)
    print arr
    print str(seq)
    print list(seq)
    assert seq.len == len(non_decreasing_seq_brute(arr))

    
def should_generate_largest_subsequence():
    assert_correct_length(array(10))
    assert_correct_length(array(10))
    assert_correct_length(array(20))
    assert_correct_length(array(15))
    assert_correct_length(array(20))
    assert_correct_length(array(30))

import timeit
def profile():

    print "100 elem DP", timeit.Timer(lambda: non_decreasing_seq(array(100))).timeit(3)
    print "1000 elem DP", timeit.Timer(lambda: non_decreasing_seq(array(1000))).timeit(3)
 #   print "5000 elem DP", timeit.Timer(lambda: non_decreasing_seq(array(5000))).timeit(1)
#    print "10000 elem DP", timeit.Timer(lambda: non_decreasing_seq(array(10000))).timeit(1)
    print "50 elem brute force", timeit.Timer(lambda: non_decreasing_seq_brute(array(50))).timeit(3)
    print "80 elem brute force", timeit.Timer(lambda: non_decreasing_seq_brute(array(100))).timeit(1)
    

if __name__ == '__main__':
    profile()