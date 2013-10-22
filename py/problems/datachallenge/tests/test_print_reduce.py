from .util import mock_console_io,  tabify
from ..reducer import consolidate, main
from ..prettyprint_mapper import format_connections, main as print_main
def should_consolidate():
    assert (list(format_connections(consolidate(['1 2 3', '1 4 5',
                                                '2 3 1', '2 5 6', '3 1 2']))) ==
            tabify(['1 2 3 4 5', '2 1 3 5 6', '3 1 2']) )

def should_sort():
    assert [tabify('foo bar baz cux zip')] == list(format_connections(
        consolidate(['foo zip baz', 'foo bar cux'])))

def should_work_end_to_end():
    with mock_console_io('''brendan torsten
                         davidbowie kim
                         davidbowie omid
                         davidbowie ziggy
                         kim davidbowie
                         kim torsten
                         mick ziggy''') as mock:
        main()
    reduce_out = mock[0]
    with mock_console_io(reduce_out) as mock:
        print_main()
    assert mock[0] == tabify(
'''brendan torsten
davidbowie kim omid ziggy
kim davidbowie torsten
mick ziggy
''')
    