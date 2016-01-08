'''
A bar of choc cantains sections of sweet and dark chocs
An optimum bar has more sweet sections than bitter
The problem is derive optimum tasting cholate bar out of the given bar, by cutting bitter parts if required The amount to wastage should be minimal

Assume bitter and sweet as sequence of 1 and -1 The overall sum should be positive for it to taste good
The bar can be cut into smaller bars adn throwing away minimal amout of bitter sections

ex:
-1,1,-1 => [1]
1,-1 => [1]
1,-1,1 => [1,-1,1]
1,-1,-1,1 => [1] [1]
1,-1,-1,1,-1,-1,1 => [1] [1] [1]
1,-1,-1,1,1 => [1] [-1,1,1]
1,1,-1,-1,1,-1,1 => [1,1,-1,-1,1,-1,1]
[-1,-1,1,1,-1] => [1,1,-1] or [-1,1,1]

'''

'''
return a list of segment [(start_index, end_index, sweetness)... ]
'''
from collections import namedtuple

Segment = namedtuple('Segment', ['i', 'j', 'sweetness'])

def tastybars_recur(bar, i=0, j=None):
    if not bar or (j is not None and  i > j):
        return []
    if j is None:
        j = len(bar) - 1

    if j == i:
        return [Segment(i, i, 1)] if bar[i] == 1 else [Segment(i, i, -1)]
    return min(merge([Segment(i, i, bar[i])], tastybars_recur(bar, i + 1, j)), 
        merge(tastybars_recur(bar, i, j - 1), [Segment(j, j, bar[j])]),
        key = weight)

'''
 return len,span of a segment
 take -ve for min() function do bigger the span- smaller the weight
 span = i of ist segment... i of last
'''
def weight(segment):
    return len(segment), -(segment[-1].j - segment[0].i) if segment else 0
    
def merge(segments1, segments2):
    print(segments1, segments2)    
    if not segments1:
        return segments2 if segments2 and segments2[0][2] > 0 else []
    if not segments2:
        return segments1 if segments1 and segments1[0][2] > 0 else []
    last, first = segments1[-1], segments2[0]

    merged_sweetness = last.sweetness + first.sweetness - (first.i - last.j - 1)
    if merged_sweetness > 0:
        return segments1[:-1] + [Segment(last.i, first.j, merged_sweetness)] + segments2[1:]
        
    if last.sweetness <= 0 and first.sweetness < 0:
        return segments1[:-1] + segments2[1:]
        
    if last.sweetness <= 0:
        return segments1[:-1] +  segments2
        
    if first.sweetness <= 0:
        return segments1 + segments2[1:]
        
    return segments1 + segments2

def sweet_segments(bar):
    i, n = 0, len(bar)
    segments = []
    while i < n:
        while i < n and bar[i] < 0:
            i += 1
        if i >= n:
            break
        start = i
        while  i < n and bar[i] > 0:
            i += 1
        end = i - 1
        segments.append(Segment(start, end, end - start + 1))
    return segments
        
def tastybars(bar):
    if not bar:
        return []
    segments = sweet_segments(bar)
    if not segments:
        return []
    print(segments)
    n = len(segments)
    dp_table = [[None] *  n for i in range(n)]
    for k in range(n):
        for i in range(n - k):
            j = i + k
            if k == 0:
                dp_table[i][j] = [segments[i]]
                continue
            dp_table[i][j] = min([merge(dp_table[i][j - l],
                                        dp_table[i + k - l - 1][j])
                                  for l in range(1, k + 1)], key = weight)
    opt_result = dp_table[0][n - 1]
    if not opt_result:
        return opt_result
    print(dp_table)
    first, last = opt_result[0], opt_result[-1]
    if first.i > 0 and first.sweetness > 1:
        expandable_by = min(first.sweetness - 1, first.i)
        opt_result[0] = Segment(first.i - expandable_by,
                                first.j,
                                first.sweetness - expandable_by)
    bar_last_i = len(bar) - 1
    if first.j < bar_last_i and last.sweetness > 1:
        expandable_by = min(last.sweetness - 1, bar_last_i - last.j)
        opt_result[-1] = Segment(last.i,
                                 last.j + expandable_by,
                                 last.sweetness - expandable_by)

    return opt_result
            

############################## TESTS ##############################

import pytest
    
def should_return_sweet_segments():
    assert (sweet_segments([ -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1]) ==
            [(1, 3, 3), (5, 6, 2), (9, 9, 1), (11, 11, 1)])
    
@pytest.mark.parametrize('algo', [tastybars])#, tastybars_recur])        
def should_optimize_sweetness(algo):
#    assert algo([-1, 1, 1]) == [Segment(0, 2, 1)]
#    assert algo([1, 1, -1]) == [Segment(0, 2, 1)]                          
#    assert algo([1, -1, 1]) == [Segment(0, 2, 1)]                      
#    assert algo([-1, -1, -1]) == []
#    assert algo([1, 1, 1]) == [Segment(0, 2, 3)]                       
#    assert algo([-1, 1, -1]) == [Segment(1, 1, 1)]                     
    assert algo([1, 1, -1, -1, 1, -1, 1]) == [Segment(0, 6, 1)]  
    assert algo([1, -1, -1, 1, -1, -1, 1]) == [(0, 0, 1), (3, 3, 1), (6, 6, 1)]       
    assert algo([1, -1, 1, -1, -1, 1, -1, 1,-1]) == [(0, 2, 1), (5, 7, 1)]
    assert algo([1, 1, 1, 1, -1, -1, -1]) == [Segment(0, 6, 1)]
    assert algo([-1, -1, -1, 1, 1, 1, 1]) == [Segment(0, 6, 1)]




def main():
    print(tastybars_recur([-1, 1, 1]))
    print(tastybars_recur([1, 1, -1]))
    print(tastybars_recur([1, -1, 1]))
    print(tastybars_recur([-1, -1, -1]))
    print(tastybars_recur([1, 1, 1]))
    print(tastybars_recur([-1, 1, -1]))
    print(tastybars_recur([1, 1, -1, -1, 1, -1, 1]))
    print(tastybars_recur([1, -1, -1, 1, -1, -1, 1]))
    print(tastybars_recur([1, -1, 1, -1, -1, 1, -1, 1,-1]))
    print(tastybars_recur([1, 1, 1, 1, -1, -1, -1]))
    print(tastybars_recur([-1, -1, -1, 1, 1, 1, 1]))
    
if __name__ == '__main__':
    main()
