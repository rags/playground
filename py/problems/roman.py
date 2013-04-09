import math

rtoi =  {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
itor = dict(zip(rtoi.values(), rtoi.keys()))

def roman_to_int(str_):
    n = len(str_)
    i = 0
    int_ = 0
    while i < n:
        val = rtoi[str_[i]]
        if i + 1 < n:
            next_val = rtoi[str_[i + 1]]
            if val < next_val:
                int_ += next_val - val
                i += 2
                continue
        int_ += val
        i += 1
    return int_

def int_to_roman(int_):
    if not int_:
        return ''
    roman = itor[1000] * (int_ // 1000)
    remaining = int_ % 1000
    if not remaining:
        return roman
    pow10 = math.floor(math.log(remaining, 10))
    while pow10 > -1:
        base_num = 10 ** pow10
        if remaining >= 9 * base_num:
            remaining -= 9 * base_num
            roman += itor[base_num] + itor[base_num * 10]
        if remaining >= 5 * base_num:
            remaining -= 5 * base_num
            roman += itor[5 * base_num]
        if remaining >= 4 * base_num:
            remaining -= 4 * base_num
            roman += itor[base_num] + itor[5 * base_num]
        while remaining < 4 * base_num and remaining >= base_num:
            roman += itor[base_num]
            remaining -= base_num
        pow10 -= 1
    return roman
        
def should_return_int_from_roman():
    assert 1   == roman_to_int('I')
    assert 2   == roman_to_int('II')
    assert 3   == roman_to_int('III')
    assert 4   == roman_to_int('IV')
    assert 5   == roman_to_int('V') == roman_to_int('VX')
    assert 8   == roman_to_int('VIII')
    assert 9   == roman_to_int('VIIII') == roman_to_int('IX')
    assert 10   == roman_to_int('X') == roman_to_int('IXI')
    assert 40  == roman_to_int('XL')
    assert 90  == roman_to_int('XC')
    assert 900  == roman_to_int('CM') == roman_to_int('DCCCC')
    assert 999  == roman_to_int('CMXCIX') 
    assert 1000 == roman_to_int('M')
    assert 1001 == roman_to_int('MI')
    assert 1900 == roman_to_int('MCM')
    assert 2008 == roman_to_int('MMVIII')
    assert 1990 == roman_to_int('MCMXC')
    assert 1999 == roman_to_int('MCMXCIX')
    assert 1954 == roman_to_int('MCMLIV')
    assert 1967 == roman_to_int('MCMLXVII')
    assert 1639 == roman_to_int('MDCXXXIX')

def should_return_roman_from_int():
    assert int_to_roman(1)   == 'I'
    assert int_to_roman(2)   == 'II'
    assert int_to_roman(3)   == 'III'
    assert int_to_roman(4)   == 'IV'
    assert int_to_roman(8)   == 'VIII'
    assert int_to_roman(9)   == 'IX'
    assert int_to_roman(5)   == 'V'
    assert int_to_roman(10)  == 'X'
    assert int_to_roman(40)  == 'XL'
    assert int_to_roman(90)  == 'XC'
    assert int_to_roman(900)  == 'CM'
    assert int_to_roman(999)  == 'CMXCIX'
    assert int_to_roman(1000) == 'M'
    assert int_to_roman(1001) == 'MI'
    assert int_to_roman(1900) == 'MCM'
    assert int_to_roman(2008) == 'MMVIII'
    assert int_to_roman(1990) == 'MCMXC'
    assert int_to_roman(1999) == 'MCMXCIX'
    assert int_to_roman(1954) == 'MCMLIV'
    assert int_to_roman(1967) == 'MCMLXVII'
    assert int_to_roman(1639) == 'MDCXXXIX'
    assert int_to_roman(9999) == 'M' * 9 + 'CMXCIX'
