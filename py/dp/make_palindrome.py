def make_palindrome_recur(str):
    return _make_palindrome_recur(str, 0, len(str) - 1)

def _make_palindrome_recur(str, i, j):
    if j == i:
        return 0
        
    if i == j - 1:
        return 0 if str[i] == str[j] else 1

    return (_make_palindrome_recur(str, i + 1, j - 1) if str[i] == str[j]
            else min(_make_palindrome_recur(str, i + 1, j), _make_palindrome_recur(str, i, j - 1)) + 1)




################################### TESTS ###################################

def should_return_no_of_ops_to_make_palindrome():
    assert make_palindrome_recur("a") == 0
    assert make_palindrome_recur("aa") == 0
    assert make_palindrome_recur("aba") == 0
    assert make_palindrome_recur("abba") == 0
    assert make_palindrome_recur("abb") == 1
    assert make_palindrome_recur("ab") == 1
    assert make_palindrome_recur("abcd") == 3
    assert make_palindrome_recur("abcde") == 4
    assert make_palindrome_recur("abbde") == 3
    assert make_palindrome_recur("abbde") == 3
    assert make_palindrome_recur("evilolive") == 0
    assert make_palindrome_recur("evilolive") == 0
    assert make_palindrome_recur("everoddoeven") == 2 #never odd or even. 2 chars missing
