#Given a list of stock prices. Buy and sell to maximize profits (can be does as many times as needed)
def buy_sell(prices):
    if not prices or len(prices) < 1:
        return

    buy_sell = []
    total_profit = 0
    min, max, profit = 0, -1, 0
    for i in range(1, len(prices)):
        cur_profit = prices[i] - prices[min]
        if profit < cur_profit:
            profit = cur_profit
            max = i
            continue
        if profit:
            total_profit += profit
            buy_sell.append((min, max))
        min, max, profit = i, -1, 0

    if profit:
        total_profit += profit
        buy_sell.append((min, max))
    return total_profit, buy_sell
    

############################## TESTS ##############################
import pytest

@pytest.mark.parametrize(('prices', 'profit', 'buy_sell_guide'), [
    ([100, 180, 260, 310, 240, 535, 695], 665, [(0, 3), (4, 6)]), 
    ([100, 180, 260, 310, 110, 535, 695], 795, [(0, 3), (4, 6)]), 
    ([100, 180, 260, 310, 1, 535, 695], 904, [(0, 3), (4, 6)]), 
    ([110, 100, 180, 260, 310, 320, 535, 695], 595, [(1, 7)]), 
    ([100, 90, 80, 70, 50, 60], 10, [(4, 5)]), 
    ([100, 90, 80, 70, 60, 60], 0, []), 
    ([30, 40, 110, 109], 80, [(0, 2)]), 
    ([100, 170, 210, 250, 120, 90, 190], 250, [(0, 3), (5, 6)]), 
])
def should_maximize_profits(prices, profit, buy_sell_guide):
    assert (profit, buy_sell_guide) == buy_sell(prices)