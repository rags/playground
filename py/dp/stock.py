# How much of stock of each company would you buy in 1991
# to maximize profit in 2011
# This is nothing but knapsack (reimplement - dont reuse)

def optimal_investment(capital_in_1991, portfolio):
    companies, val_1991, val_2011 = zip(*portfolio)
    dp_table = [[(0, []) for i in range(len(companies) + 1)] for j in range(capital_in_1991 + 1)]

    for money_in_1991 in range(1, capital_in_1991 + 1):
        for stock in range(1, len(companies) + 1):
            # The default value ensures you have same amount of money in 2011
            # even if you dont invest or you get to keep money remaining after investment
            buy_current = (money_in_1991, []) 
            if money_in_1991 >= val_1991[stock - 1]:
                remaining = dp_table[money_in_1991 - val_1991[stock - 1]][stock]
                buy_current = (val_2011[stock - 1] + remaining[0],
                               [companies[stock - 1]] + remaining[1])
            dp_table[money_in_1991][stock] = max(
                buy_current, 
                dp_table[money_in_1991][stock - 1]
            )
    return dp_table[capital_in_1991][len(companies)]
            
            
############################## TESTS ##############################
#(company,stock value in 1991,stock value in 2011)
portfolio = [
    ('Dale, Inc.', 12, 39), 
    ('JCN Corp.', 10, 13), 
    ('Macroware, Inc.', 18, 47), 
    ('Pear, Inc.', 15, 45)
]

def should_maximize_profit():
    assert (50, ['Pear, Inc.']) == optimal_investment(20, portfolio)
    assert (90, ['Pear, Inc.', 'Pear, Inc.']) == optimal_investment(30, portfolio)
    assert (390, ['Dale, Inc.'] * 10) == optimal_investment(120, portfolio)

    