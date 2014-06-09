from math import ceil, floor

def sqrt(n):
    GOOD_ENUF = .000000001
    sqrt_ = n / 2
    while abs(n - sqrt_ ** 2) > GOOD_ENUF:
        sqrt_ = (sqrt_ + (n / sqrt_)) / 2
    return sqrt_


def nearest_perfect_sq(n):
    sqrt_ = sqrt(n)
    if sqrt_ - int(sqrt_) > .5:
        return ceil(sqrt_) ** 2
    return floor(sqrt_) ** 2
    

############################## TESTS ##############################

def should_find_perfect_square():
    assert 25 == nearest_perfect_sq(23)
    assert 16 == nearest_perfect_sq(20)
    assert 25 == nearest_perfect_sq(21)
    assert 9 == nearest_perfect_sq(12)
    assert 81 == nearest_perfect_sq(90)
    assert 100 == nearest_perfect_sq(92)
