map =  {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman_to_int(str_):
    n = len(str_)
    i = 0
    int_ = 0
    while i < n:
        val = map[str_[i]]
        if i + 1 < n:
            next_val = map[str_[i + 1]]
            if val < next_val:
                int_ += next_val - val
                i += 2
                continue
        int_ += val
        i += 1
    return int_


def should_return_int_from_roman():
    assert 1   == roman_to_int('I')
    assert 2   == roman_to_int('II')
    assert 3   == roman_to_int('III')
    assert 8   == roman_to_int('VIII')
    assert 4   == roman_to_int('IV')
    assert 40  == roman_to_int('XL')
    assert 90  == roman_to_int('XC')
    assert 900  == roman_to_int('CM')
    assert 1000 == roman_to_int('M')
    assert 1001 == roman_to_int('MI')
    assert 1900 == roman_to_int('MCM')
    assert 900 == roman_to_int('DCCCC')
    assert 2008 == roman_to_int('MMVIII')
    assert 1990 == roman_to_int('MCMXC')
    assert 1954 == roman_to_int('MCMLIV')
    assert 1967 == roman_to_int('MCMLXVII')
    