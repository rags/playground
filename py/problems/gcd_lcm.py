from collections import Iterable

def _apply(*args,**kwargs):
    if not args:
        return
    if len(args) == 1:
        return reduce(kwargs['fn'], args[0]) if isinstance(args[0], Iterable) else args[0]
    return reduce(kwargs['fn'], args)

def gcd(*args):
    return _apply(*args, fn = _gcd)
    
def lcm(*args):
    return _apply(*args, fn = _lcm)

def _gcd(x, y):
    x, y = min(x, y), max(x, y)
    while(x!= 0):
        x, y = y % x, x
    return y

def _lcm(x, y):
    return x * y / _gcd(x, y)


############################## TESTS ##############################

def should_find_gcd():
    assert not gcd()
    assert 5 == gcd(5)
    assert 5 == gcd([5])
    assert 5 == gcd(5, 10, 15)
    assert 5 == gcd([20, 25, 15])
    assert 3 == gcd({9, 12, 15})
    assert 5 == gcd({5: [], 10: [], 15: []})
    assert 1 == gcd(5, 7, 9)

def should_find_lcm():
    assert 5 == lcm([5])
    assert 30 == lcm(5, 10, 15)
    assert 12 == lcm(4, 3)
    assert 12 == lcm(6, 4, 3, 12)
    assert 18 == lcm(3, 6, 9, 18)
