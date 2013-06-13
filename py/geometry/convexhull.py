from . import Pt, Ln
from slope import compare, find_left_right
import functools


def outmost(pts, origin):
    def _min(pt1, pt2):
        return pt1 if compare(pt1, pt2, origin) > 0 else pt2
    return reduce(_min, [pt for pt in pts if pt != origin])

# O(n^2), O(nh) to be more precise. where h is no of nodes that form the hull.
# Worst case n=h, where convex hull is made up of all points in the input.
def convex_hull_n2(pts): 
    cur = left_most = min(pts)
    hull = []
    i = 0
    while True:
        i += 1
        hull.append(cur)
        cur = outmost(pts, cur)
        if i > len(pts) ** 2:
            break
        if cur == left_most:
            break
    return hull

def convex_hull_nlogn(pts):
    left_most = min(pts)
    #sort - O(nlog(n))
    sorted_pts = sorted(pts, cmp=functools.partial(compare, origin=left_most))
    hull = [left_most, sorted_pts.pop(0), sorted_pts.pop(0)]
    for pt in sorted_pts:#O(n)
        while find_left_right(Ln(hull[-1], hull[-2]), pt) < 0: #left turn
            hull.pop()
        hull.append(pt)
    return hull
            
    
    
################################### TESTS ###################################

import pytest

@pytest.mark.parametrize(('algorithm'), [convex_hull_n2, convex_hull_nlogn])
@pytest.mark.parametrize(('pts', 'hull'), [
    
    ([Pt(30, 30),Pt(50, 60), Pt(60, 20), Pt(70, 45),
      Pt(86, 39), Pt(112, 60), Pt(200, 113), Pt(250, 50),
      Pt(300, 200), Pt(130, 240), Pt(76, 150), Pt(47, 76),
      Pt(36, 40), Pt(33, 35), Pt(30, 30)],
     [Pt(60, 20), Pt(250, 50), Pt(300, 200),
      Pt(130, 240), Pt(76, 150), Pt(47, 76), Pt(30, 30)]),
    
    ([Pt(50, 60), Pt(60, 20), Pt(70, 45), Pt(100, 70),
      Pt(125, 90), Pt(200, 113), Pt(250, 140),  Pt(180, 170),
      Pt(105, 140),  Pt(79, 140),  Pt(60, 85)],
     [Pt(60, 20), Pt(250, 140), Pt(180, 170), Pt(79, 140), Pt(50, 60)]),
    
    ([Pt(60, 20), Pt(250, 140), Pt(180, 170), Pt(79, 140), Pt(50, 60)],
     [Pt(60, 20), Pt(250, 140), Pt(180, 170), Pt(79, 140), Pt(50, 60)])])
def should_plot_convex_hull(pts, hull, algorithm):
    assert set(hull) == set(algorithm(pts))



@pytest.mark.parametrize(('hull', 'algorithm'),
                         [([Pt(0, 0), Pt(0, 10), Pt(10, 0), Pt(10, 10)],
                           convex_hull_n2),
                          ([Pt(x=0,  y=0), Pt(x=10,  y=10),
                            Pt(x=9,  y=10), Pt(x=0,  y=10),
                            Pt(x=1,  y=10), Pt(x=10,  y=0)],
                           convex_hull_nlogn)])
    
def should_find_hull_when_points_on_hull(hull, algorithm):
    assert set(hull) == set(algorithm([Pt(0, 0), Pt(0, 10), Pt(10, 0),
                                       Pt(10, 10), Pt(2, 3), Pt(3, 9),
                                       Pt(9, 9), Pt(5, 5), Pt(9, 1),
                                       Pt(7, 7), Pt(9, 10), Pt(1, 10)]))
