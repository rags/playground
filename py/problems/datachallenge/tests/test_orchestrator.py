from .util import tabify, untabify, mock_console_io
from ..orchestrator import pow2factors, orchestrate, main

def should_return_pow2_factors():
    assert [8, 4, 2, 1] == list(pow2factors(15))
    assert [8, 2, 1] == list(pow2factors(11))
    assert [32] == list(pow2factors(32))
    assert [1] == list(pow2factors(1))

     
LINEAR_NETWORK_SIZE = 100
def neighbors_at_length(no_of_hops):
    network = []
    for i in range(1, LINEAR_NETWORK_SIZE + 1):
        str_range = sorted(map(str, range(max(1, i - no_of_hops),
                                          min(LINEAR_NETWORK_SIZE + 1, i + no_of_hops + 1))))
        str_range.remove(str(i))
        str_range.insert(0, str(i))
        network.append('\t'.join(str_range))
    network.sort()
    return network

def should_work_for_longer_hops(): #takes over 30s to complete
    #1->2->3->4 ...... 99->100
    LINEAR_NETWORK = ['%d\t%d' % pair for pair in zip(
        range(1,LINEAR_NETWORK_SIZE),
        range(2,LINEAR_NETWORK_SIZE + 1))]
    for i in range(1, LINEAR_NETWORK_SIZE):
        assert neighbors_at_length(i) == list(orchestrate(LINEAR_NETWORK, i))

    
def should_work_for_the_given_input():
    with mock_console_io(tabify(
'''davidbowie  omid
davidbowie  kim
kim         torsten
torsten     omid
brendan     torsten
ziggy       davidbowie
mick        ziggy
''')) as out:
        main(2)
        
    assert out[0] == tabify(
'''brendan kim omid torsten
davidbowie kim mick omid torsten ziggy
kim brendan davidbowie omid torsten ziggy
mick davidbowie ziggy
omid brendan davidbowie kim torsten ziggy
torsten brendan davidbowie kim omid
ziggy davidbowie kim mick omid
''')


