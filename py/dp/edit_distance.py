COPY = 1
ADD = 2
DEL = 2
REPLACE = 3
TWIDDLE = 4
KILL = 2

'''
suffix DP
edit_distance of src,target is
 max{
       ADD target[-1] + edit_dist(src, target[:-1])
       DEL src[-1] + edit_dist(src[:-1], target)
       REPLACE src[-1] with target[-1] + edit_dist(src[:-1], target[:-1])
       COPY src[-1] with target[-1] edit_distance(src[:-1],target[-1]) if src[-1]==target[-1]
       TWIDDLE src[-1] and src[-2] edit_distance(src[:-2],target[-2]) if src[-2:]==target[-2:]
    }
'''

def edit_dist_recur(src, target):
    if not (src or target):
        return (0, [])
    if not src:
        return (len(target) * ADD, ['ADD ' + target])
    if not target:
        #const cost to del all extra chars
        return (KILL, ['KILL ' + src])
        
    if src[-1] == target[-1]:
        s = edit_dist_recur(src[:-1], target[:-1])
        return (COPY + s[0]), s[1] + ['COPY ' + src[-1]]
    if len(src) >= 2 and len(target) >= 2 and (src[-2], src[-1]) == (target[-1], target[-2]):
        s = edit_dist_recur(src[:-2], target[:-2])
        return TWIDDLE + s[0], s[1] + ['TWIDDLE ' + src[-2:]]

    s1, s2, s3 = (edit_dist_recur(src, target[:-1]),
                  edit_dist_recur(src[:-1], target),
                  edit_dist_recur(src[:-1], target[:-1]))
    min_ = min(
        (ADD + s1[0], s1[1] + ['ADD ' + target[-1]]), 
        (DEL + s2[0], s2[1] + ['DEL ' + src[-1]]), 
        (REPLACE + s3[0], s3[1] + ['REPLACE %s with %s' % (src[-1], target[-1])]), 
    )
    return min_

#O(n^2)
def edit_dist(src, target):
    m, n = len(src), len(target)
    dp = [[None for i in range(n + 1)] for j in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == j == 0:
                dp[i][j] = (0, [])
                continue
            if i == 0:
                dp[i][j] = (j * ADD, ['ADD ' + target[:j]])
                continue
            if j == 0:
                dp[i][j] = (KILL, ['KILL ' + src[:i]])
                continue
                
            if src[i - 1] == target[j - 1]:
                dp[i][j] = (COPY + dp[i - 1][j - 1][0]), dp[i - 1][j - 1][1] + ['COPY ' + src[i - 1]]
                continue
            if i > 1 and j > 1 and (src[i - 2], src[i - 1]) == (target[j - 1],
                                                                target[j - 2]):
                dp[i][j] = TWIDDLE + dp[i - 2][j - 2][0], dp[i - 2][j - 2][1] + ['TWIDDLE ' + src[i - 2: i]]
                continue
            dp[i][j] = min((ADD + dp[i][j - 1][0], dp[i][j - 1][1] + ['ADD ' + target[j - 1]]), 
                           (DEL + dp[i - 1][j][0], dp[i - 1][j][1] + ['DEL ' + src[i - 1]]), 
                           (REPLACE + dp[i - 1][j - 1][0], dp[i - 1][j - 1][1] + ['REPLACE %s with %s' % (src[i - 1], target[j - 1])]))
            
#    print dp
    return dp[m][n]
                

############################## TESTS ##############################
    
import pytest

@pytest.mark.parametrize('algorithm', [edit_dist_recur, edit_dist])
def should_calc_edit_distance(algorithm):
    assert ((20,  ['COPY a', 'COPY l', 'DEL g', 'REPLACE o with t', 'COPY r', 'ADD u',
                  'COPY i', 'ADD s', 'COPY t', 'REPLACE h with i', 'REPLACE m with c']) ==
            algorithm('algorithm', 'altruistic'))
    assert (7, ['TWIDDLE no', 'REPLACE p with e']) == algorithm('nop', 'one')
    assert (2, ['KILL foo']) == algorithm('foo', '')
    assert (6, ['ADD foo']) == algorithm('', 'foo')

    assert (7, ['KILL n','COPY o', 'COPY p', 'COPY e', 'ADD n']) == algorithm('nope', 'open')

    assert ((18, ['KILL sh', 'ADD p', 'COPY o', 'COPY w', 'COPY e', 'COPY r', 'COPY  ',
                 'ADD s', 'REPLACE p with h', 'COPY o', 'COPY w', 'COPY e', 'COPY r']) ==
            algorithm('shower power', 'power shower'))
    
    