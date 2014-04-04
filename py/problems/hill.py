
def hill(v):
    print "b", v
    diff = 0
    for i in range(0,len(v)-1):
        a, b = v[i], v[i + 1]
        if a >= b:
            d = (a - b + 1)
            v[i + 1] += d
            if d > diff:
                diff = d
    print "a", v
    return diff


import random
def should_work():
    for i in range(10):
        
        a = range(10)
        random.shuffle(a)
        hill(a)
        print  "\n"

    assert 0