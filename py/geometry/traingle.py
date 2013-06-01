from . import Pt
from slope import in_between

#tells if pt is bound by triangle formed by pt1,pt2,pt3
def pt_in_triangle((pt1, pt2, pt3), pt):
    return in_between(pt, pt2, pt3, pt1) and in_between(pt, pt1, pt2, pt3)

################################### TESTS ###################################
import pytest

@pytest.mark.parametrize(('triangle', 'in_pts', 'out_pts'), [
((Pt(1, 1), Pt(2, 4), Pt(3, 3)), [Pt(2, 2)], [Pt(1, 2), Pt(1, 4)]),
((Pt(2, 2), Pt(2, 10), Pt(10, 2)), [Pt(6, 6), Pt(4, 4), Pt(3, 8), Pt(9, 3)],
 [Pt(10, 10), Pt(7, 7), Pt(9, 4), Pt(1, 1)]), 
((Pt(10, 10), Pt(2, 10), Pt(10, 2)),
 [Pt(10, 10), Pt(7, 7), Pt(9, 4), Pt(6, 6), Pt(9, 3), Pt(6, 7)],
 [Pt(4, 4), Pt(4, 4), Pt(3, 8), Pt(1, 1), Pt(2, 3)])    
])
def should_tell_if_pt_is_bound_by_triangle(triangle, in_pts, out_pts):
    assert all([pt_in_triangle(triangle, pt) for pt in in_pts ])
    assert all([not pt_in_triangle(triangle, pt) for pt in out_pts])

    
    