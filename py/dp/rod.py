#cut rod (or not) of lenght n into pieces so that the net value is maximized
# based in price table which contains price for rod lenghts 0..n

# return value,pieces
# O(n^2)
def cut(n, price_table):
    dp = {}
    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[(i, j)] = (0, [])
                continue
            if i > j:
                dp[(i, j)] = dp[(i - 1, j)]
                continue
            dp[(i, j)] = max(((price_table[i] + dp[(i,j - i)][0]),
                              [i] + dp[(i,j - i)][1]), dp[i - 1, j])
    return dp[(n, n)]

############################## TESTS ##############################

def should_cut_rods_profitably():
    price_table = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    for n,expected in enumerate([(1, [1]), (5, [2]), (8, [3]), (10, [2, 2]), (13, [3, 2]),
                                 (17, [6]), (18, [6, 1]), (22, [6, 2]), (25, [6, 3]),
                                 (30, [10])], start=1):
        assert cut(n, price_table) == expected
