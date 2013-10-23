import sys
from functools import reduce
from itertools import chain
from math import log2
from path_doubling_mapper import link_combinations as path_double
from one_hop_mapper import link_combinations as one_hop
from reducer import consolidate
from prettyprint_mapper import format_connections
from combine_mapper import combine
from combine_reducer import extend_paths

def merge(onto, from_):
    return consolidate(sorted(extend_paths(sorted(combine(
        chain(onto, format_connections(from_)))))))

def orchestrate_logn(network, n):
    dp_table = {}
    for i in range(int(log2(n)) + 1):
        network = list(consolidate(sorted(path_double(network))))
        cur_pow2 = 2 ** i
        if n & cur_pow2 == cur_pow2: #only store if pow2 bit is set in n
            dp_table[cur_pow2] = network
    if len(dp_table) == 1:
        return format_connections(dp_table[n])
    return format_connections(reduce(merge, (dp_table[i] for i in sorted(dp_table.keys(), reverse = True))))

def orchestrate_O_of_n(network, n):
    for i in range(n):
        network = list(consolidate(sorted(one_hop(network))))
    return format_connections(network)

def main(n=2, algorithm=orchestrate_logn):
    for user_network in algorithm(sys.stdin, n):
        print(user_network)

if __name__ == '__main__':
    main()

