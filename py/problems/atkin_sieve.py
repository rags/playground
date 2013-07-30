# program to generate prime numbers upto a certain given number
# Uses most recent/fast algo from 2004- http://en.wikipedia.org/wiki/Sieve_of_Atkin
import math
import itertools

def count_primes(limit):
    return len(primes_upto(limit))

def primes_upto(limit):
    if limit < 5:
        return {2, 3} if limit >= 3 else {2} if limit == 2 else set()
    n=int(math.ceil(math.sqrt(limit)))
    primes = {2,3}
    for x in range(1,n+1):
        for y in range(1,n+1):
            num = 4*x**2+y**2
          
            if (num <= limit) and (num % 12 == 1 or num % 12 == 5):
                primes.add(num) if num not in primes else primes.remove(num)
            num = 3*x**2+y**2
            
            if (num <= limit) and (num % 12 == 7):
                primes.add(num) if num not in primes else primes.remove(num)
            
            if (x > y): 
                num= 3*x**2-y**2
                
                if (num <= limit) and (num % 12 == 11):
                    primes.add(num) if num not in primes else primes.remove(num)
    #print primes    
    for i in range(5,n):
        if i in primes:
            i2=i**2
            for a in itertools.count(1):
                num=a*i2
                if num>limit:
                    break
                if num in primes:
                    primes.remove(num)
    return primes


############################## TESTS ##############################
first_few_primes = [
      2,      3,      5,      7,     11,     13,     17,     19,     23,     29,
     31,     37,     41,     43,     47,     53,     59,     61,     67,     71,
     73,     79,     83,     89,     97,    101,    103,    107,    109,    113,
    127,    131,    137,    139,    149,    151,    157,    163,    167,    173,
    179,    181,    191,    193,    197,    199,    211,    223,    227,    229,
    233,    239,    241,    251,    257,    263,    269,    271,    277,    281,
    283,    293,    307,    311,    313,    317,    331,    337,    347,    349,
    353,    359,    367,    373,    379,    383,    389,    397,    401,    409,
    419,    421,    431,    433,    439,    443,    449,    457,    461,    463,
    467,    479,    487,    491,    499,    503,    509,    521,    523,    541,
    547,    557,    563,    569,    571,    577,    587,    593,    599,    601,
    607,    613,    617,    619,    631,    641,    643,    647,    653,    659,
    661,    673,    677,    683,    691,    701,    709,    719,    727,    733,
    739,    743,    751,    757,    761,    769,    773,    787,    797,    809,
    811,    821,    823,    827,    829,    839,    853,    857,    859,    863,
    877,    881,    883,    887,    907,    911,    919,    929,    937,    941,
    947,    953,    967,    971,    977,    983,    991,    997,   1009,   1013 ]
def should_genrate_primes():
    for i in [1, 2, 3, 4, 5, 7, 8, 10, 100, 500, 1000, 1013]:
        assert primes_upto(i) == set([p for p in first_few_primes if p <= i])

def should_count_primes():
    
    for pow, prime_cnt in enumerate([0, 4, 25, 168, 1229, 9592, 78498 ]):
        assert prime_cnt == count_primes(10 ** pow) 
        