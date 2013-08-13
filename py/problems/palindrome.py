from __future__ import print_function
import math

#O(log10(n)) <- O(log10(n)/2)
def is_palindrome_int(x):
    i = 10 ** int(math.log(x,10))
    j = 10
    while i>=j:
        a=x//i%10
        b=x%j//(j//10)
        if a != b:
            return False
        i=i//10
        j=j*10
    return True

def dp_entry_cmp(entry):
    return len(entry[0])
def longest_palindrome_dp(seq):
    n = len(seq)
    #holds(longest_palin,bool to indicate dp[i,j] itself is a palindrome)
    dp_table = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        dp_table[i][i] = (seq[i: i+1], True)
    for k in range(n - 1):
        for i in range(n - k - 1):
            j = i + k + 1
            if k == 0:
                dp_table[i][j] = ((dp_table[i][i][0], False) if seq[i] != seq[j] else
                (seq[i:j + 1], True))
            else:
                if seq[i] == seq[j] and dp_table[i + 1][j - 1][1]:
                    dp_table[i][j] = (seq[i:j + 1], True)
                else:
                    dp_table[i][j] = (max(dp_table[i][j - 1], dp_table[i + 1][j],
                                          key = lambda entry: len(entry[0]))[0], False)
#    for row in dp_table:
#        print()
#        for cell in row:
#            if cell:
#                print(cell[0], end = ' ')
#            
    return dp_table[0][n - 1][0]
                    
    
def longest_palindrome_recur(seq):
    if len(seq) < 4:
        if seq[0] == seq[-1]:
            return seq
        return seq[0:1]
    if seq[0] == seq[-1]:
        for i in range(1, len(seq) // 2):
            if seq[i] != seq[-i-1]:
                return max(longest_palindrome_recur(seq[1:]),
                           longest_palindrome_recur(seq[:- 1]), key = len)
        return seq
    else:
        return max(longest_palindrome_recur(seq[1:]),
                           longest_palindrome_recur(seq[:-1]), key = len)
            

#O(n^2)
'''
palins[k] contains 1/2 the length of longest palindrome centered around
i - where k=1*2 - odd lenght palindrome
i,i+1 - where k=i*2+1- even length palidrome

aba - palins[2]=1
abba - palins[3]=2 (center of palindrome is between i,i+1 where i=2 and k=3 (i*2+1))
'''        
def longest_palindrome_n2(seq):
    n = len(seq)
    i = 0
    palins = [0] * (n * 2 - 1)
    while i < n:
        k, l, cnt = i - 1, i + 1, 0
        while k > -1 and l < n and seq[k] == seq[l]:
            cnt += 1
            k -= 1
            l += 1
        palins[i * 2] = cnt
        if i + 1 < n:
            k, l, cnt = i, i + 1, 0
#            print(i, k, l, seq[k], seq[l])
            while k > -1 and l < n and seq[k] == seq[l]:
                cnt += 1
                k -= 1
                l += 1
            palins[i * 2 + 1] = cnt
        i += 1
    #print(palins)
    max_ = 0
    for i, val in enumerate(palins):
        if val > palins[max_]:
            max_ = i
    
    return (seq[max_ // 2 - palins[max_] + 1: max_ // 2 + palins[max_] + 1]  if max_ % 2 == 1
            else seq[max_ // 2 - palins[max_]: max_ // 2 + palins[max_] + 1])
    

# O(n) - most fucked up piece of code I ever wrote.
# Explanation - http://www.akalin.cx/longest-palindrome-linear-time
def longest_palindrome(seq):
    n = len(seq)
    i = 0
    palins = [0] * (n * 2 - 1)
    max_ = 0
    #XX = 0 # for testing time
    while i < n:
        if n - i - 1 < palins[max_]:
#            print("done", i, n, max_, palins[max_])
            break
        if (n - 1) - (i + 1) >= palins[max_]:
            cnt = palins[i * 2]
            k, l = i - 1 - cnt, i + 1 + cnt
            while k > -1 and l < n and seq[k] == seq[l]:
                cnt += 1
                k -= 1
                l += 1
            palins[i * 2] = cnt
            if cnt > palins[max_]:
                max_ = i * 2
            #XX += cnt
        if i + 1 < n:
            cnt = palins[i * 2 + 1]
            k, l = i - cnt, i + 1 + cnt
            while k > -1 and l < n and seq[k] == seq[l]:
                cnt += 1
                k -= 1
                l += 1
            palins[i * 2 + 1] = cnt
#            if i == 1:
#                print("here",i * 2 + 1, palins[i * 2 + 1])
            if cnt > palins[max_]:
                max_ = i * 2 + 1
            #XX += cnt
        next = i + max(min(palins[i * 2], palins[i * 2 + 1]), 1)
        for j in range(1, max(palins[i * 2] * 2 , palins[i * 2 + 1] * 2)):
            idx = i * 2 + 1 - j
            if palins[idx]:
                #print(idx // 2)
                next = (i * 2 + 1 + j)// 2
                break
        assert next > i, (palins, i, i * 2, i * 2 + 1, next)
        i = next
        #XX += 1
        #print(i, palins)
    #print("L=", len(seq), "O=", XX)
#    print(palins[max_], max_)
    return (seq[max_ // 2 - palins[max_] + 1: max_ // 2 + palins[max_] + 1] if max_ % 2 == 1
            else seq[max_ // 2 - palins[max_]: max_ // 2 + palins[max_] + 1])
    
    
        
############################## TESTS ##############################

if __name__ == '__main__':
    print(longest_palindrome('abcbabccbabcbaaaaa'))
    print(longest_palindrome('abcbabccbabcba'))
    
import pytest

def should_detect_int_palidrome():
    assert is_palindrome_int(31044013)
    assert is_palindrome_int(3104013)
    assert not is_palindrome_int(1214)

@pytest.mark.parametrize('algorithm', [longest_palindrome_recur,
                                       longest_palindrome_dp,
                                       longest_palindrome_n2, longest_palindrome])
def should_return_longest_contigious_palidrome(algorithm):
    assert 'abcbabccbabcba' == algorithm('abcbabccbabcbaaaaa')
    assert 'baxab' == algorithm('baxybaxab')
    assert 'aibohphobia' == algorithm('aibohphobia')
    assert 'abcbabcbabcba' == algorithm('abcbabcbabcba')
    assert 'abcbabccbabcba' == algorithm('abcbabccbabcba')
    assert 'abcbabcba' == algorithm('abcdabcbabcba')
    assert 'abadaba' == algorithm('yabadabadoo')
    assert 'anana' == algorithm('bananas')
    assert 'ababaababa' == algorithm('acababaababab')
    assert 'aaaa' == algorithm('aaaa')
    assert '01044010' == algorithm('014101044010414')
    assert [3, 0, 1, 0, 1, 0, 3] == algorithm([1, 0, 3, 0, 1, 0, 1, 0, 3, 2, 1])
    assert 'abaxxaba' == algorithm('babaxxaba')
    #assert algorithm != longest_palindrome