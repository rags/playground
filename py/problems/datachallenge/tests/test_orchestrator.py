from ..orchestrator import pow2factors, orchestrate

def should_return_pow2_factors():
    assert [8, 4, 2, 1] == list(pow2factors(15))
    assert [8, 2, 1] == list(pow2factors(11))
    assert [32] == list(pow2factors(32))
    assert [1] == list(pow2factors(1))

     
LINEAR_NETWORK_SIZE = 10
def neighbors_at_length(no_of_hops):
    network = []
    for i in range(1, LINEAR_NETWORK_SIZE + 1):
        str_range = sorted(map(str, range(max(1, i - no_of_hops),
                                          min(LINEAR_NETWORK_SIZE + 1, i + no_of_hops + 1))))
        str_range.remove(str(i))
        str_range.insert(0, str(i))
        network.append(' '.join(str_range))
    network.sort()
    return network

def should_work_for_longer_hops():
    #1->2->3->4 ...... 99->100
    LINEAR_NETWORK = ['%d %d' % pair for pair in zip(
        range(1,LINEAR_NETWORK_SIZE),
        range(2,LINEAR_NETWORK_SIZE + 1))]
    for i in range(6, 7):
        print (neighbors_at_length(i))
        print (list(orchestrate(LINEAR_NETWORK, i)))
        assert neighbors_at_length(i) == list(orchestrate(LINEAR_NETWORK, i))

    
def should_work_for_the_given_input():
    assert ('\n'.join(orchestrate(
'''davidbowie  omid
davidbowie  kim
kim         torsten
torsten     omid
brendan     torsten
ziggy       davidbowie
mick        ziggy
'''.split('\n'), 2)) ==
'''brendan kim omid torsten
davidbowie kim mick omid torsten ziggy
kim brendan davidbowie omid torsten ziggy
mick davidbowie ziggy
omid brendan davidbowie kim torsten ziggy
torsten brendan davidbowie kim omid
ziggy davidbowie kim mick omid'''
            )
