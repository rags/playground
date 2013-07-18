#Find longest subsequence thats a palindrome
'''
substring dp
recurrence relation:
  lps(str) = {
         lps(str[i:n-1]) if str[0]==str[n-1]
         else
         max {
            lps(str[1:]),lps(str[:n-1])
         }
  }
explanation: the longest palidrome will have last and fist char equal - rest is contained within this substring that follows, else try with reduced subproblem on left and right

'''

def lps(seq):
    n = len(seq)
    dp_table = [['' for i in range(n)] for i in range(n)]
    for i in range(n):
        dp_table[i][i] = seq[i]
    for i in range(n - 1):
        for j in range(n - i - 1):
            x, y = j, i + j + 1
            if seq[x] == seq[y]:
                dp_table[x][y] = (seq[x] + dp_table[x + 1][y - 1] + seq[y])
            else:
                dp_table[x][y] = max(dp_table[x][y - 1], dp_table[x + 1][y], key = len)
    print dp_table
    return dp_table[0][n - 1]
                
############################## TESTS ##############################

def should_find_lps():
    assert lps('axya') in ['axa', 'aya']
    assert lps('aWbXccYbZa') in ['abccba']
    assert 'carac' == lps('character')
    assert 'aibohphobia' == lps('i do not have aibohphobia')
    assert 'civic' == lps('honda civic')
    assert 'race ecar' == lps('race the car')
    assert 'dhihd' == lps('deepthigchandramowli')
            

