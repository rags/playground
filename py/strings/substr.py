'''
Complexity worst case O(mn).
The worst case has very low probability.
probability that first char matches is 1/26 and 2nd char match is 1/(26^2)
'''
def index_Omn(text, substr):
    m, n = len(substr), len(text)
    i = 0
    while i < n:
        j = 0
        while j < m and text[i + j] == substr[j]:
            j += 1
        if j == m:
            return i
        i += 1
    return -1

'''
Knuth-Morris-Pratt (KMP)- An algorithm to check if a String is a substring of another.
http://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
O(n+m)
'''
def index(text, substr):
#    print text
#    print substr
    m, n = len(substr), len(text)
    partial_match = KMP_table(substr)
#    print partial_match
    i, j = 0, 0
    while i + j < n:
        if text[i + j] == substr[j]:
            if j == m - 1:
                return i
            j += 1
        else:
#            print "mismatch i+j=%s, i=%s, j=%s, T[j]=%s" % (i + j, i, j, partial_match[j])
            i = i + j - partial_match[j]
            j = partial_match[j] if partial_match[j] > -1 else 0
#            print "reset i+j=%s, i=%s, j=%s" % (i + j, i, j)
    return -1
                

#makes the partial match table for substr    
def KMP_table(substr):
    table = [-1, 0]
    i, j = 2, 0
    while i < len(substr):
        if substr[i - 1] == substr[j]:
            j += 1
            table.append(j)
            i += 1
        elif j > 0:
            j = table[j]
        else:
            table.append(0)
            i += 1
    return table
        
        
############################## TESTS ##############################
import pytest

@pytest.mark.parametrize('algorithm', [index_Omn, index])
@pytest.mark.parametrize(('str_','sub', 'at'), [
('ABC ABCDAB ABCDABCDABDE', 'ABCDABD', 15), 
('This is some random piece of text', 'is', 2), 
('This is some random piece of text', 'blah', -1), 
('and some more random and more', 'ando', 15), 
('and some more random and more', 'and more', 21), 
])
def should_return_substring_index(str_, sub, at, algorithm):
    assert at == algorithm(str_, sub)
    if at >- 1:
        assert str_[at: at + len(sub)] == sub
 #   assert algorithm != index
        
def should_construct_partial_match_table():
    assert [-1, 0, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 1, 0, 1] == KMP_table('aabbaabbaababaa')
    assert [-1, 0, 0, 0, 0, 1, 2] == KMP_table('abcdabd')
    assert ([-1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0, 0, 0]
            == KMP_table('participate in parachute'))

