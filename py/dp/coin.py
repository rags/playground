def combinations_recur(denoms, amount):
    return _combinations_recur(sorted(denoms), amount, [[]]) or []
    
def _combinations_recur(denoms, amount, combs):
    #print denoms, amount
    if amount == 0:
        return combs
    if not denoms:
        return
    denom0 = denoms[0]
    if denom0 > amount:
        return
    combs_without_demon0 = _combinations_recur(denoms[1:], amount, combs) 
    combs_with_demon0 = _combinations_recur(denoms, amount - denom0, combs)
    if combs_with_demon0 is not None:
        combs_with_demon0 = [comb + [denom0] for comb in combs_with_demon0]
        
    if combs_with_demon0 and combs_without_demon0:
        return combs_with_demon0 + combs_without_demon0
    
    return combs_without_demon0 or combs_with_demon0


def combinations_dp(denoms, amount):
    bags = {0: [[]]}
    denoms = sorted(denoms)
    for amt in range(1, amount + 1):
        bags[amt] = []
        for denom in denoms:
            if denom <= amt:
                bags[amt].extend(map(lambda comb: comb + [denom], bags[amt - denom]))
    return bags[amount]



def _min_comb(comb1, comb2):
    return comb2 if len(comb2) < len(comb1) else comb1

def best_combination(denoms, amount):
    bags = {0: [[]]}
    denoms = sorted(denoms)
    for amt in range(1, amount + 1):
        bags[amt] = []
        for denom in denoms:
            if denom <= amt and bags[amt - denom]:
                bags[amt].append(reduce(_min_comb , bags[amt - denom]) + [denom])
    return reduce(_min_comb, bags[amount])

                
        
############################## TESTS ##############################
import pytest
def are_equal(expected, actual):
    expected, actual = sorted(map(sorted, expected)), sorted(map(sorted, actual))
    for e in expected:
        assert e in actual

def should_return_best_combination():
    assert [2] == best_combination([2, 1], 2)
    assert [5,  5] == best_combination([2, 5, 3, 6], 10)
    assert [25, 25, 10] == best_combination([25, 10, 5, 1], 60)



@pytest.mark.parametrize('algorithm', [combinations_recur, combinations_dp])
def should_find_combinations_for_change(algorithm):
    are_equal([[1, 1], [2]], algorithm([2, 1], 2))
    are_equal([[2, 2, 2, 2, 2], [3, 3, 2, 2], [6, 2, 2], [5, 3, 2], [5,  5]],
              algorithm([2, 5, 3, 6], 10))
    are_equal([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [10, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [5, 5, 5, 5, 1, 1, 1, 1, 1],
               [10, 5, 5, 1, 1, 1, 1, 1], [10, 10, 1, 1, 1, 1, 1], [5, 5, 5, 5, 5],
               [10, 5, 5, 5], [10, 10, 5], [25]], algorithm([25, 10, 5, 1], 25))





