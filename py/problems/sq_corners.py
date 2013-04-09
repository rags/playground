def is_square(pt1, pt2, pt3, pt4):
    all_pts = [pt1, pt2, pt3, pt4]
    min_x = min(all_pts)[0]
    min_y = min(all_pts, key = lambda pt: pt[1])[1]
    max_x = max(all_pts)[0]
    max_y = max(all_pts, key = lambda pt: pt[1])[1]
    return (max_x - min_x == max_y - min_y and
            any((min_x, min_y) == pt for pt in all_pts) and
            any((max_x, max_y) == pt for pt in all_pts) and
            any((max_x, min_y) == pt for pt in all_pts) and
            any((min_x, max_y) == pt for pt in all_pts))

def should_identify_a_square():
    assert is_square((3, 4), (7, 8), (3, 8), (7,4))
    assert is_square((2, 2), (-2, 2), (2, -2), (-2,-2))
    assert is_square((1, 1), (0, 0), (0, 1), (1, 0))
    assert not is_square((1, 1), (0, 0), (0, 1), (1, 1))
    assert not is_square((3, 4), (8, 8), (3, 8), (8,4)) #rectangle
