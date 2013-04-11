# find min range x,y in lists l1,l2, l3... such that range x..y (x,y inclusive)
# contains atleast one element from each list
def min_covering_range(*args):
    idx = [0] * len(args)
    min_range = None
    while True:
        sorted_lst_heads = sorted([(args[i][j], i) for i, j in enumerate(idx)])
        mn, mx = sorted_lst_heads[0][0], sorted_lst_heads[-1][0]
        if not min_range or mx - mn < min_range[1] - min_range[0]:
            min_range =  mn, mx
        if not any(j < len(args[i]) - 1 for i, j in enumerate(idx)):
            return min_range
        for _, i in sorted_lst_heads:
            if idx[i] < len(args[i]) - 1:
                idx[i] += 1
                break
        
def dumbest_thing_that_i_could_first_think_of(lst1, lst2, lst3):
    i = j = k = 0
    maxi, maxj, maxk = len(lst1) - 1, len(lst2) - 1, len(lst3) - 1
    min_range = None
    while True:
        ip, jp, kp = i, j, k
        mn, mx = min(lst1[i], lst2[j], lst3[k]), max(lst1[i], lst2[j], lst3[k])
        if mn == lst1[i]:
            if i < maxi:
                i += 1
            else:
                if lst2[j] <= lst3[k] and  k < maxk:
                    k += 1
                elif j < maxj:
                    j += 1
                elif k < maxk:
                    k += 1
        elif mn == lst2[j]:
            if j < maxj:
                j += 1
            else:
                if lst1[i] <= lst3[k] and i < maxi:
                    i += 1
                elif k < maxk:
                    k += 1
                elif i < maxi:
                    i += 1

        elif mn == lst3[k]:
            if k < maxk: 
                k += 1
            else:
                if lst1[i] <= lst2[j] and i < maxi:
                    i += 1
                elif j < maxj:
                    j += 1
                elif i < maxi:
                    i += 1

        #print i, j, k
        #print "M", min_range
        #print "C", mn, mx
        if not min_range or mx - mn < min_range[1] - min_range[0]:
            min_range =  mn, mx
        if i == ip and j == jp and k == kp: #nothing changed
            assert i == maxi and j == maxj and k == maxk
            return min_range
        
        
def should_find_min_range():
    assert (20, 24) == min_covering_range([4,  10,  15,  24,  26],
                                          [0,  9,  12,  20],
                                          [5,  18,  22,  30])

    assert (100, 101) == min_covering_range([101, 1001, 1050],
                                           [5, 50, 100, 150, 200, 300, 400, 500, 600, 700, 8000],
                                           [10, 20, 30, 50, 100])
    assert (87, 93) == min_covering_range([25,  31,  50,  52,  61,  69,  76,  93],
                                    [13,  30,  87],
                                    [4,  15,  38,  50,  62,  73,  74,  74,  90])


def min_range_brute(*args):
    min_range = None
    for comb in cross_join(*args):
        mn, mx = min(comb), max(comb)
        if not min_range or mx - mn < min_range[1] - min_range[0]:
            min_range = mn, mx
    return min_range
        
def cross_join(*args):
    cross = []
    for l in args:
        tmp = []
        for e in l:
            if not cross:
                tmp.append([e])
            else:
                for lst in cross:
                    tmp1 = lst[:]
                    tmp1.append(e)
                    tmp.append(tmp1)
        cross = tmp
    return cross
    
from numpy import random as rand
def should_word_for_random():
    for i in range(20):
        lists = []
        for i in range(rand.randint(2, 6)):
            lists.append(sorted(rand.randint(0, 100, size=rand.randint(3, 10))))
        
        brute_result = min_range_brute(*lists)
        assert min_covering_range(*lists) == brute_result
