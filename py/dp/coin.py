from itertools import groupby
from functools import reduce

def combinations_recur(denoms, amount):
    return _combinations_recur(sorted(denoms), amount, []) or []
'''
for some N amount and K numbers.
T(N,K) = T(N,K-1) + T(N-1,K) assuming there are K 1's
The tree goes N*K=X deep
So T(N,K) = T(X) = 2T(X-1)=2^(X-1)=2^N*K-1= O(2^K*N)
'''
def _combinations_recur(denoms, amount, combs):
    #print denoms, amount
    if amount == 0:
        return combs
    if not denoms:
        return
    denom0 = denoms[0]
    if denom0 > amount:
        return
    combs_without_denom0 = _combinations_recur(denoms[1:], amount, combs)
    combs_with_denom0 = _combinations_recur(denoms, amount - denom0, combs)

    if combs_with_denom0 is not None:
        if not combs_with_denom0:
            combs_with_denom0 = [{}]
        for comb in combs_with_denom0: comb[denom0] = comb.get(denom0, 0) + 1


    if combs_with_denom0 and combs_without_denom0:
        return unique_combs(combs_with_denom0, combs_without_denom0)

    return combs_without_denom0 or combs_with_denom0

def unique_combs(combs1, combs2 = None):
    combs = combs1 if not combs2 else (combs1 + combs2)
    if not combs: return combs
    return [k for k, v in groupby(sort(combs))]

def sort(listofmap):
    return sorted(listofmap,  key = lambda m: sorted(m.items()))

#O(N*K)
def combinations_dp(denoms, amount):
    bags = {0: [{}]}
    denoms = sorted(denoms)
    for amt in range(1, amount + 1):
        bags[amt] = []
        for denom in denoms:
            if denom <= amt:
                bags[amt] =  unique_combs(bags[amt] + list(map(lambda comb: extend(comb, denom), bags[amt - denom])))
    return bags[amount]

def extend(combs, denom):
    ret_comb =  combs.copy()
    ret_comb[denom] =  ret_comb.get(denom, 0) + 1
    return ret_comb

def _min_comb(comb1, comb2):
    return comb1 if sum(comb1.values()) <= sum(comb2.values()) else comb2

def best_combination(denoms, amount):
    bags = {0: [{}]}
    denoms = sorted(denoms)
    for amt in range(1, amount + 1):
        bags[amt] = []
        for denom in denoms:
            if denom <= amt and bags[amt - denom]:
                bags[amt].append(extend(reduce(_min_comb , bags[amt - denom]), denom))
    return reduce(_min_comb, bags[amount])



############################## TESTS ##############################
import pytest

def assert_eq(expected,  actuals):
    assert sort(expected) == sort(actuals)

def should_return_best_combination():
    assert {2: 1} == best_combination([2, 1], 2)
    assert {5: 2} == best_combination([2, 5, 3, 6], 10)
    assert {25: 2, 10: 1} == best_combination([25, 10, 5, 1], 60)


@pytest.mark.parametrize('algorithm', [combinations_recur,  combinations_dp])
def should_find_combinations_for_change(algorithm):
    assert_eq([{1: 2}, {2: 1}], algorithm([2, 1], 2))
    assert_eq([{2: 5}, {3: 2, 2: 2}, {6: 1, 2: 2}, {5: 1, 3: 1, 2: 1}, {5: 2}], algorithm([2, 5, 3, 6], 10))
    assert_eq([{10: 1, 5: 2, 1: 5}, {5: 4, 1: 5}, {10: 2, 1: 5}, {10: 1, 5: 1, 1: 10}, {5: 3, 1: 10}, {5: 2, 1: 15}, {10: 1, 1: 15}, {5: 1, 1: 20}, {1: 25}, {10: 2, 5: 1}, {10: 1, 5: 3}, {5: 5}, {25: 1}], algorithm([25, 10, 5, 1], 25))
