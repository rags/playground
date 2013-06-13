from . import Pt, Ln
# compare slopes of 2 lines (origin,pt1) and (origin,pt2)
# slope = (y2-y1)/(x2-x1)
# to compare 2 ratios a/b and c/d cmp(a*d, c*b)
def compare(pt1, pt2, origin=Pt(0, 0), compare_same_slope_points = True):
    sp1, sp2 = slope(origin, pt1), slope(origin, pt2)
    r1, r2 = sp1.y * sp2.x, sp2.y * sp1.x
    #print pt1, pt2, origin
    #print sp1, sp2, r1, r2
    if r1 == r2: #pt1,pt2 on same line
        if not compare_same_slope_points:
            return 0
        if pt1.x == pt2.x: # same horizontal line
            return 2 if pt1.y > pt2.y else -2 if pt2.y > pt1.y else 0
        return 3 if pt1.x > pt2.x else -3
    return cmp(r1, r2)
            
'''
0   := pt is on line
< 0 := pt left of line
> 0 := pt right of line
'''
def find_left_right(line, pt):
    return compare(line.pt2, pt, line.pt1, False)
    
def slope(pt1, pt2):
    return Pt(pt2.x - pt1.x, pt2.y - pt1.y)

#is point in between the slope created by (origin,pt1) and (origin,pt2)
def in_between(pt, pt1, pt2, origin):
    return compare(pt, pt1, origin) != compare(pt, pt2, origin)
    
############################## TESTS ##############################

def should_tell_if_pt_lies_left_or_right():
    assert find_left_right(Ln(Pt(0, 0), Pt(1, 5)), Pt(2, 3)) > 0 #right
    assert find_left_right(Ln(Pt(0, 0), Pt(1, 5)), Pt(1, 3)) > 0 #right
    assert find_left_right(Ln(Pt(0, 0), Pt(2, 3)), Pt(1, 4)) < 0 #right
    assert find_left_right(Ln(Pt(1, 1), Pt(2, 2)), Pt(3, 3)) == 0 #right
def should_compare_point_position():
    assert 0 == compare(Pt(2, 2), Pt(2, 2))
    assert 0 > compare(Pt(2, 2), Pt(3, 3))
    assert 0 > compare(Pt(8, 2), Pt(-8, 2))
    assert 0 < compare(Pt(8, 2), Pt(-8, -2))
    assert 0 < compare(Pt(8, 2), Pt(8, -2))
    assert 0 < compare(Pt(3, 2), Pt(3, 1))
    assert 0 < compare(Pt(1, 5), Pt(2, 3))
    assert 0 < compare(Pt(1, 5), Pt(1, 4))
    assert 0 > compare(Pt(1, 0), Pt(4, 0))
    assert 0 < compare(Pt(1, 4), Pt(4, 4))
    assert 0 < compare(Pt(1, 3), Pt(2, 3), Pt(1, 2))
