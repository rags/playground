def make_palindrome_recur(str):
    return _make_palindrome_recur(str, 0, len(str) - 1)

def _make_palindrome_recur(str, i, j):
    if j == i:
        return 0
        
    if i == j - 1:
        return 0 if str[i] == str[j] else 1

    return (_make_palindrome_recur(str, i + 1, j - 1) if str[i] == str[j]
            else min(_make_palindrome_recur(str, i + 1, j), _make_palindrome_recur(str, i, j - 1)) + 1)



'''
DP loop
| 00 | 01 | 02 | 03 | 04 |
| -- | 11 | 12 | 12 | 14 |
| -- | -- | 22 | 23 | 24 |
| -- | -- | -- | 33 | 34 |
| -- | -- | -- | -- | 44 |
'''

def make_palindrome(str):
    n = len(str)
    if n == 1:
        return 0
    dp_tbl = [[None for i in range(n)] for j in range(n)]
    for k in range(n):
        for i in range(n - k):
            j = i + k
            if k == 0:
                dp_tbl[i][j] = str[i], 0
                continue
            if k < 2: #for 1st 2 loops
                if str[i] == str[j]:
                    dp_tbl[i][j] = str[i] + str[j], 0
                else: # make 'xy'-> 'xyx'- a palindrome
                    dp_tbl[i][j] = str[i] + str[j] + str[i], 1
                continue
            if str[i] == str[j]:
                sub_palindrome, insertions = dp_tbl[i + 1][j - 1]
                dp_tbl[i][j] = str[i] + sub_palindrome + str[i], insertions
                continue
            (sub_palindrome1, insertions1) = dp_tbl[i + 1][j]
            (sub_palindrome2, insertions2) = dp_tbl[i][j - 1]
            if(insertions1 <= insertions2):
                dp_tbl[i][j] = str[i] + sub_palindrome1 + str[i], insertions1 + 1
            else:
                dp_tbl[i][j] = str[j] + sub_palindrome2 + str[j], insertions2 + 1

    palindrome, insertions = dp_tbl[0][n - 1]
    print("palindrome for '%s' is '%s' with %d insertions" % (str, palindrome, insertions))
    return insertions
                
            
################################### TESTS ###################################

def should_return_no_of_ops_to_make_palindrome():
    assert make_palindrome("a") == 0
    assert make_palindrome("aa") == 0
    assert make_palindrome("aba") == 0
    assert make_palindrome("abba") == 0
    assert make_palindrome("abb") == 1
    assert make_palindrome("ab") == 1
    assert make_palindrome("abcd") == 3
    assert make_palindrome("abcde") == 4
    assert make_palindrome("abbde") == 3
    assert make_palindrome("abbde") == 3
    assert make_palindrome("evilolive") == 0
    assert make_palindrome("eil-liv") == 2
    assert make_palindrome("everoddoeven") == 2 #never odd or even. 2 chars missing
