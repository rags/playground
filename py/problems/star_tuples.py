def star_tuple(tup):
    if not tup:
        return tuple()
    return map(tuple, _star(list(tup)))

def _star(elements):
    if len(elements) == 1:
        return [['*'], elements]
    combs = _star(elements[1:])
    return [['*'] + comb for comb in combs] + [elements[0:1] + comb for comb in combs]


def should_provide_all_combinations_with_star():
    assert star_tuple((1,)) == [('*', ), (1, )]
    assert star_tuple(('A','B')) == [('*', '*'), ('*', 'B'), ('A', '*'), ('A', 'B')]
    assert star_tuple((1, 2, 3)) == [('*', '*', '*'),  ('*', '*', 3),  ('*', 2,  '*'),  ('*', 2,  3),  (1,  '*', '*'),  (1,  '*', 3),  (1,  2,  '*'),  (1,  2,  3)]
    four_tuple_combs = star_tuple((1, 2, 3, 4))
    assert 16 == 2 ** 4
    assert four_tuple_combs == [('*', '*', '*', '*'),  ('*', '*', '*', 4),  ('*', '*', 3,  '*'),  ('*', '*', 3,  4),  ('*', 2,  '*', '*'),  ('*', 2,  '*', 4),  ('*', 2,  3,  '*'),  ('*', 2, 3, 4), (1,  '*', '*', '*'), (1,  '*', '*', 4), (1,  '*', 3, '*'), (1,  '*', 3, 4), (1,  2,  '*', '*'), (1,  2,  '*', 4), (1,  2,  3,  '*'), (1,  2,  3,  4)]

    