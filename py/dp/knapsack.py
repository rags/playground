'''
recurrence for n-size,m-items:
optimal_sack(n,m) = max{
                          optimal_sack(n,m-1) - dont take the item
                          val(m) + optimal_sack(n-weight(m),m-1) - take the item
                       }
'''

def optimal_sack_recur(knapsack_size, items):
    if not (items and knapsack_size):
        return 0
    weight, value = items[0]
    return max(value + optimal_sack_recur(knapsack_size - weight, items)
               if weight <= knapsack_size else 0,
               optimal_sack_recur(knapsack_size, items[1:]))
'''
O(Nm) - pseudo polynomial
N - sack size (its an integer input)
m - no of items
O(Nm) = O(2^n*m) where n = log(N) and hence the knapsack is exp for large N 
'''        
def optimal_sack(knapsack_size, items):
    weights, values = zip(*items)
    dp_table = [[0 for i in range(len(items) + 1)] for j in range(knapsack_size + 1)]
    for sack_size in range(1, knapsack_size + 1):
        for j in range(1, len(items) + 1):
            item_weight = weights[j - 1]
            if sack_size < item_weight:
                dp_table[sack_size][j] = 0
                continue
            dp_table[sack_size][j] = max(dp_table[sack_size][j - 1],
                                 values[j - 1] + dp_table[sack_size - item_weight][j])

    print(dp_table)
    return dp_table[knapsack_size][len(items)]


############################## TESTS ##############################
import pytest

@pytest.mark.parametrize('algorithm', [optimal_sack, optimal_sack_recur])
def should_calc_best_knapsack(algorithm):
    36 == algorithm(15, [(12, 4), (2, 2), (1, 1), (4, 10), (1, 2)])
    70 == algorithm(100, [(100, 40), (50, 35), (45, 18), (20, 4), (10, 10), (5, 2)])
    35 + 18 == algorithm(99, [(100, 40), (50, 35), (45, 18), (20, 4), (10, 10), (5, 2)])
    #assert 0
