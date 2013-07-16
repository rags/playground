#http://en.wikipedia.org/wiki/Longest_increasing_subsequence
#Suffix problem
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
        
    def __len__(self):
        return self.len
        
    def __cmp__(self, other):
        return self.len.__cmp__(other.len)

    def __iter__(self):
        node = self.root
        while node is not None:
            yield node.value
            node = node.next_node
            
    def __str__(self):
        return str(self.root)
#O(n^2)
def non_decreasing_seq_tree(seq):
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
    return list(reversed(list(max(subseqs))))

#O(n^2)
def non_decreasing_seq(seq):
    if not seq:
        return []
    n = len(seq)
    subseqs = [None] * n
    for i in range(n - 1, -1, -1):
        choices = [seq[i:i + 1]]
        for j in range(i + 1, n):
            if seq[i] <= seq[j]:
                choices.append(seq[i:i + 1] + subseqs[j] )
        subseqs[i] = max(choices, key=len)
    return max(subseqs, key=len)


############################## TESTS ##############################
import pytest    
from intro_to_algos.sort.arrays import array
from longest_inc_sub_seq_brute import non_decreasing_seq_brute

def assert_correct_length(arr, algorithm):
    assert len(algorithm(arr)) == len(non_decreasing_seq_brute(arr))


@pytest.mark.parametrize('algorithm', [non_decreasing_seq_tree, non_decreasing_seq])
@pytest.mark.parametrize(('input', 'expected'),
                         [([4, 5, 1, 6, 2, 3, 4], [1, 2, 3, 4]),
                          ([6, 2, 3, 8, 1, 5, 2, 6, 1, 4, 7, 8], [2, 3, 5, 6, 7, 8]),
                          ([5, 13, 8, 12, 2, 21, 3, 15, 7, 1, 9, 11, 6, 17, 10, 16, 29,
                            22, 4, 26, 23, 20, 18, 14, 19, 27, 30, 25, 28, 24],
                           [2, 3, 7, 9, 11, 17, 22, 26, 27, 30])])
def should_generate_largest_subsequence(input, expected, algorithm):
    assert expected == list(algorithm(input))
    
    
@pytest.mark.parametrize('algorithm', [non_decreasing_seq_tree, non_decreasing_seq])    
def should_generate_largest_subsequence_random_input(algorithm):
    assert_correct_length(array(10), algorithm)
    assert_correct_length(array(10), algorithm)
    assert_correct_length(array(20), algorithm)
    assert_correct_length(array(15), algorithm)
    assert_correct_length(array(20), algorithm)
    assert_correct_length(array(30), algorithm)

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