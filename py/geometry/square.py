from . import Pt
def is_square(pt1, pt2, pt3, pt4):
    pt1, pt2, pt3, pt4 = sorted([pt1, pt2, pt3, pt4])
    return ((pt1.x == pt2.x and pt3.x == pt4.x and
            pt1.y == pt3.y and pt2.y == pt4.y) #A rectangle
            and (pt1.y - pt2.y) == (pt2.x - pt3.x)) #height==lenght

############################## TESTS ##############################
    
def should_tell_if_4_pts_make_a_square():
    assert is_square(Pt(1, 1), Pt(10, 10), Pt(1, 10), Pt(10, 1))
    assert not is_square(Pt(1, 1), Pt(10, 9), Pt(1, 9), Pt(10, 1))
    #rhombus
    assert not is_square(Pt(-3, 2), Pt(-2, 6), Pt(2, 7), Pt(1, 3))
