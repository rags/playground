#Filter from set nCk to just return numbers that add upto n
def combinations(n, k):
    all_combs = []
    _combinations(range(1, n + 1),n, k,[], all_combs)
    return all_combs

def _combinations(a, n, k, cur, all_combs):
    if len(cur) == k and sum(cur) == n:
        all_combs.append(cur)
        return
    if sum(cur) >= n or len(cur) >= k:
        return
    if not a:
        return
    _combinations(a[1:], n, k, cur + [a[0]], all_combs)
    _combinations(a[1:], n, k, cur, all_combs)

    
    
    
############################## TESTS ##############################

def should_return_right_combinations():
    assert {(1, 5), (2, 4)} == set(map(tuple, combinations(6, 2)))
    assert {(4, 6), (1, 9), (2, 8), (3, 7)} == set(map(tuple, combinations(10, 2)))
    assert {(1,  2,  7),  (1,  3,  6),  (1,  4,  5),  (2,  3,  5)} == set(map(tuple, combinations(10, 3)))
    assert {(1,  2,  3, 4)} == set(map(tuple, combinations(10, 4)))
    
