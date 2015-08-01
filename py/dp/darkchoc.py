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
    
def merge(segment1,  segment2):
    if not segment1:
        return segment2 if segment2 and segment2[0][2] > 0 else []
    if not segment2:
        return segment1 if segment1 and segment1[0][2] > 0 else []
    last, first = segment1[-1], segment2[0]

    merged_sweetness = last.sweetness + first.sweetness - (first.i - last.j - 1)
    if merged_sweetness > 0:
        return segment1[:-1] + [Segment(last.i, first.j, merged_sweetness)] + segment2[1:]
        
    if last.sweetness <= 0 and first.sweetness < 0:
        return segment1[:-1] + segment2[1:]
        
    if last.sweetness <= 0:
        return segment1[:-1] +  segment2
        
    if first.sweetness <= 0:
        return segment1 + segment2[1:]
        
    return segment1 + segment2


############################## TESTS ##############################
    
def should_optimize_sweetness():
    assert tastybars_recur([-1, 1, 1]) == [Segment(0, 2, 1)]
    assert tastybars_recur([1, 1, -1]) == [Segment(0, 2, 1)]                          
    assert tastybars_recur([1, -1, 1]) == [Segment(0, 2, 1)]                      
    assert tastybars_recur([-1, -1, -1]) == []
    assert tastybars_recur([1, 1, 1]) == [Segment(0, 2, 3)]                       
    assert tastybars_recur([-1, 1, -1]) == [Segment(1, 1, 1)]                     
    assert tastybars_recur([1, 1, -1, -1, 1, -1, 1]) == [Segment(0, 6, 1)]  
    assert tastybars_recur([1, -1, -1, 1, -1, -1, 1]) == [(0, 0, 1), (3, 3, 1), (6, 6, 1)]       
    assert tastybars_recur([1, -1, 1, -1, -1, 1, -1, 1,-1]) == [(0, 2, 1), (5, 7, 1)]
    assert tastybars_recur([1, 1, 1, 1, -1, -1, -1]) == [Segment(0, 6, 1)]
    assert tastybars_recur([-1, -1, -1, 1, 1, 1, 1]) == [Segment(0, 6, 1)]




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
