from .util import tabify, untabify, mock_console_io
from orchestrator import (orchestrate_logn,
                            main,  orchestrate_O_of_n)
import pytest
import random
     
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

@pytest.mark.parametrize('algorithm',
                         [orchestrate_logn, orchestrate_O_of_n])
def should_work_for_longer_hops(algorithm): 
    #1->2->3->4 ...... 99->100
    LINEAR_NETWORK = ['%d\t%d' % pair for pair in zip(
        range(1,LINEAR_NETWORK_SIZE),
        range(2,LINEAR_NETWORK_SIZE + 1))]
    for i in range(1, LINEAR_NETWORK_SIZE, random.randint(5, 10)):
        assert neighbors_at_length(i) == list(algorithm(LINEAR_NETWORK, i))

@pytest.mark.parametrize('algorithm',
                         [orchestrate_logn, orchestrate_O_of_n])
def should_work_for_the_given_input(algorithm):
    with mock_console_io(tabify(
'''davidbowie  omid
davidbowie  kim
kim         torsten
torsten     omid
brendan     torsten
ziggy       davidbowie
mick        ziggy
''')) as out:
        main(2, algorithm)
        
    assert out[0] == tabify(
'''brendan kim omid torsten
davidbowie kim mick omid torsten ziggy
kim brendan davidbowie omid torsten ziggy
mick davidbowie ziggy
omid brendan davidbowie kim torsten ziggy
torsten brendan davidbowie kim omid
ziggy davidbowie kim mick omid
''')


