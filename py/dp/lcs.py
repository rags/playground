#Find longest common subsequence between 2 sequences

#O(2^n) - all combinations of a sequence 
def all_combs(seq):
    if len(seq) == 1:
        return [seq[0:0], seq[0:1]]
    combs = all_combs(seq[1:])
    add_to = seq[0: 1].__add__
    return combs + map(add_to, combs)

#O(n*2^m)  m,n = len(s1),len(s2)
def lcs_brute(s1, s2):
    combs = all_combs(s1)
    longest = s2[0:0]
    for comb in combs:
        if len(comb) > len(s2):
            continue
        i = 0
        for c in s2:
            if i >= len(comb):
                break
            if comb[i] == c:
                i += 1
        if i == len(comb) and i > len(longest):
            longest = comb
    return longest

'''
T(m,n) = T(m-1,n-1) or T(m,n-1)+T(m-1,n) - latter is worst case
depth of tree = m+n
shape of tree = binary
O(m,n)=2^2(m+n)
exponential
'''
def lcs_recur(s1, s2):
    if not (s1 and s2):
        return s1[0:0]
        
    if s1[-1] == s2[-1]:
        return lcs_recur(s1[:-1], s2[:-1]) + s1[-1:]
    return max(lcs_recur(s1, s2[:-1]), lcs_recur(s1[:-1], s2), key = len)

#O(mn)- space & time
def lcs(seq1, seq2):
    empty = seq1[:0]
    m, n = len(seq1) + 1, len(seq2) + 1
    dp_table = [[empty for i in range(m)] for j in range(n)]
    for k in range(1, n):
        for l in range(1, m):
            i, j = l - 1, k - 1
            dp_table[k][l] = (dp_table[j][i] + seq1[i:l] if seq1[i] == seq2[j]
                              else max(dp_table[j][l], dp_table[k][i], key = len))
    #print dp_table
    return dp_table[n - 1][m - 1]

'''
Space - O(min(m,n))
Time - O(mn)
'''
def lcs_space_optimal(seq1, seq2):
    s1 = min(seq1, seq2, key=len)
    s2 = seq2 if s1 == seq1 else seq1
    empty = s1[:0]
    m, n = len(s1) + 1, len(s2) + 1
    memo, cur = [empty for i in range(m)], [empty for i in range(m)]
    for k in range(1, n):
        memo = cur[:]
#        print memo
        for l in range(1, m):
            i, j = l - 1, k - 1
            cur[l] = (memo[i] + s1[i:l] if s1[i] == s2[j]
                              else max(memo[l], cur[i], key = len))
#    print cur
    return cur[m - 1]
            

############################## TESTS ##############################
import pytest

def is_subseq(str_, sub):
    i = 0
    for j in range(len(sub)):
        c = sub[j]
        while c != str_[i]:
            i += 1
            if i >= len(str_):
                return False
    return True
    
@pytest.mark.parametrize(('s1', 's2', 'subseqs'),
                         [('AAACCGTGAGTTATTCGTTCTAGAA', 'CACCCCTAAGGTACCTTTGGTTC',
                           ['ACCTAGTATTGTTC', 'ACCTGGTTTTGTTC']),
                          ('XMJYAUZ', 'MZJAWXU', ['MJAU'])
                      ])
def should_be_sub_seq(s1, s2, subseqs):
    for subseq in subseqs:
        assert is_subseq(s1, subseq) 
        assert is_subseq(s2, subseq) 
    

def should_return_all_combinations():
    assert all_combs([1, 2, 3, 4]) == [[],  [4],  [3],  [3,  4],  [2],  [2,  4],  [2,  3],
                                       [2,  3,  4],  [1],  [1,  4],  [1,  3],  [1,  3,  4],
                                       [1,  2],  [1,  2,  4],  [1,  2,  3],  [1,  2,  3,  4]]

    assert all_combs('abcd') == ['', 'd', 'c', 'cd', 'b', 'bd', 'bc', 'bcd', 'a', 'ad',
                                 'ac', 'acd', 'ab', 'abd', 'abc', 'abcd']

    assert all_combs(('a', 1, 'b')) == [(), ('b',), (1,), (1, 'b'), ('a',), ('a', 'b'),
                                        ('a', 1), ('a', 1, 'b')]


@pytest.mark.parametrize('algorithm', [lcs_brute, lcs_recur, lcs, lcs_space_optimal])
@pytest.mark.parametrize(('s1', 's2', 'lcses'),
                         [('BANANA', 'ATANA', ['AANA']),
                          ('ABCDEFG', 'BCDGK', ['BCDG']),
                          ('XMJYAUZ', 'MZJAWXU', ['MJAU']),
                          ('nanto', 'nematode knowledge', ['nano', 'nato']),
                          
                          (['A', 'G', 'G', 'T', 'A', 'B'],
                           ['G', 'X', 'T', 'X', 'A', 'Y', 'B'], [['G', 'T', 'A', 'B']]),
                          ((1, 2, 2, 3, 1, 4), (2, 5, 3, 5, 1, 6, 4), [(2, 3, 1, 4)]),

                      ])
def should_find_lcs(s1, s2, lcses, algorithm):
    assert algorithm(s1, s2) in lcses


@pytest.mark.parametrize('algorithm', [lcs, lcs_space_optimal])
@pytest.mark.parametrize(('s1', 's2', 'lcses'),
                         [('AAACCGTGAGTTATTCGTTCTAGAA', 'CACCCCTAAGGTACCTTTGGTTC',
                           ['ACCTAGTATTGTTC', 'ACCTGGTTTTGTTC']),
                          ('empty!bottle', 'nematode knowledge', ['emtole']),
                      ])
def should_find_lcs_long_inputs(s1, s2, lcses, algorithm):
    assert algorithm(s1, s2) in lcses
