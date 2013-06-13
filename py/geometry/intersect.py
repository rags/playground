from __future__ import division
from slope import find_left_right
from . import Ln, Pt
'''
Assumption: (dont know if this assumption is mathematically sound)
if l1,l2 are segments of same line, it is not considered as intersection
lines (0,0),(5,5) and (1,1),(6,6) dont intersect- they both lie on slope x-y=0
'''
def intersect(l1, l2):
    dir1, dir2 = find_left_right(l1, l2.pt1), find_left_right(l1, l2.pt2)
    return not((dir1 > 0 and dir2 > 0)  or (dir1 < 0 and dir2 < 0) or (dir1==dir2==0))

#http://en.wikipedia.org/wiki/Line-line_intersection
def pt_of_intersection(l1, l2):
    x1, x2, x3, x4 = l1.pt1.x, l1.pt2.x, l2.pt1.x, l2.pt2.x
    y1, y2, y3, y4 = l1.pt1.y, l1.pt2.y, l2.pt1.y, l2.pt2.y
    denom =  (x1 - x2) * (y3 - y4) - (x3 - x4) * (y1 - y2)
    if not denom:
        return
    A,B = (x1 * y2 -  y1 * x2), (x3 * y4 -  y3 * x4)
    return Pt(
        (A * (x3 - x4) - (x1 - x2) * B) / denom,
        (A * (y3 - y4) - (y1 - y2) * B) / denom,
    )
    

############################## TESTS ##############################
    
def should_find_pt_of_intersection():
    assert Pt(-0.14285714285714285, 0.0) == pt_of_intersection(
        Ln(Pt(-1,-3), Pt(1, 4)), Ln(Pt(-3, 0), Pt(2, 0)))
    assert Pt(0, 0) == pt_of_intersection(Ln(Pt(0,0), Pt(1, 4)), Ln(Pt(0, 0), Pt(2, 3)))
    assert Pt(0, 3) == pt_of_intersection(Ln(Pt(0,0), Pt(0, 5)), Ln(Pt(0, 3), Pt(2, 3)))
    assert Pt(0, 3) == pt_of_intersection(Ln(Pt(0,0), Pt(0, 5)), Ln(Pt(0, 3), Pt(-2, 3)))
    assert Pt(5.5, 5.5) == pt_of_intersection(Ln(Pt(1,1), Pt(10, 10)), Ln(Pt(1, 10), Pt(10, 1)))
    assert not pt_of_intersection(Ln(Pt(1,1), Pt(5, 5)), Ln(Pt(2, 2), Pt(7, 7)))
    assert not pt_of_intersection(Ln(Pt(2,1), Pt(6, 5)), Ln(Pt(2, 2), Pt(7, 7)))
    
def should_tell_if_lines_intersect():
    assert intersect(Ln(Pt(-1,-3), Pt(1, 4)), Ln(Pt(-3, 0), Pt(2, 0)))
    assert intersect(Ln(Pt(0,0), Pt(1, 4)), Ln(Pt(0, 0), Pt(2, 3)))
    assert intersect(Ln(Pt(0,0), Pt(0, 5)), Ln(Pt(0, 3), Pt(2, 3)))
    assert intersect(Ln(Pt(0,0), Pt(0, 5)), Ln(Pt(0, 3), Pt(-2, 3)))
    assert intersect(Ln(Pt(1,1), Pt(10, 10)), Ln(Pt(1, 10), Pt(10, 1)))
    assert not intersect(Ln(Pt(0,0), Pt(1, 4)), Ln(Pt(5, 5), Pt(2, 3)))
    assert not intersect(Ln(Pt(1,1), Pt(5, 5)), Ln(Pt(2, 2), Pt(7, 7)))
    assert not intersect(Ln(Pt(2,1), Pt(6, 5)), Ln(Pt(2, 2), Pt(7, 7)))

