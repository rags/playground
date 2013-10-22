import sys
from functools import reduce
from itertools import chain
from math import log2
from mapper import link_combinations
from reducer import consolidate

def orchestrate(network, n):
    path_fragments = []
    for i in range(int(log2(n)) + 1):
        network = list(consolidate(sorted(link_combinations(network))))
        cur_pow2 = 2 ** i
        if n & cur_pow2 == cur_pow2:
            path_fragments.append(network)
    if len(path_fragments) == 1:
        return path_fragments[0]
    print(len(path_fragments))
    if len(path_fragments) > 1:
        print(path_fragments[0])
        print(path_fragments[1])
    return consolidate(sorted(reduce(chain, path_fragments)))

def main(n):
    for user_network in orchestrate(sys.stdin, n):
        print(user_network)

if __name__ == '__main__':
    main(2)


def pow2factors(n):
    assert n > 0
    while n > 0:
        pow2 = 2 ** int(log2(n))
        yield pow2
        n = n - pow2

def hadoop_orchestrate():
    pass

def sh_orchestrate():
    pass 
