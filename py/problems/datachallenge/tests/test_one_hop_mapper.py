from one_hop_mapper import main
from .util import mock_console_io, tabify

def should_work_end_to_end():
    input = ['1 2', '3 4', '5 6 7']
    expected = ['1 2', '2 1', 
                '3 4', '4 3', 
                '5 6 7', '6 5 7', '7 5 6']
    with mock_console_io(tabify('\n'.join(input))) as (out, _):
        main()
    assert out.getvalue() == tabify('\n'.join(expected) + '\n')
    
def should_handle_extended_network():
    input = tabify('''1 2 # 3
2 1 3 # 4
3 2 4 # 1 5
4 3 5 # 2 6''')
    with mock_console_io(input) as (out, _):
        main()
    assert out.getvalue() == tabify('''1 2 # 3
2 # 1 3
2 1 3 # 4
1 # 2 3 4
3 # 2 1 4
3 2 4 # 1 5
2 # 3 4 1 5
4 # 3 2 1 5
4 3 5 # 2 6
3 # 4 5 2 6
5 # 4 3 2 6
''')
 
 