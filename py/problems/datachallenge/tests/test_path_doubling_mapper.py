from path_doubling_mapper import link_combinations, main
from tests.util import mock_console_io, tabify, untabify
    
def should_generate_friend_of_friends_list_for_n_X_2_degree():
    assert  ['p1 p2 p3 p5', 'p2 p1 p3 p5',
             'p3 p1 p2 p5', 'p5 p1 p2 p3', #output for line1

             'p2 p4 p5 p6', 'p4 p2 p5 p6', #line2 output
             'p5 p2 p4 p6', 'p6 p2 p4 p5'
         ] == untabify(link_combinations(tabify(['p1 p2 p3 p5', 'p2 p4 p5 p6'])))
    
def should_map_friends_at_degree_1():
    assert tabify(['kim omid', 'omid kim',
            'omid mick', 'mick omid',
            'mick qux', 'qux mick',
            'qux kim', 'kim qux']) == list(link_combinations(tabify(["kim omid",
                                                                "omid mick",
                                                                "mick qux", 
                                                                "qux kim"])))
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
3 # 1 2
2 1 3 # 4
1 # 2 3 4
3 # 2 1 4
4 # 2 1 3
3 2 4 # 1 5
2 # 3 4 1 5
4 # 3 2 1 5
1 # 3 2 4 5
5 # 3 2 4 1
4 3 5 # 2 6
3 # 4 5 2 6
5 # 4 3 2 6
2 # 4 3 5 6
6 # 4 3 5 2\n''')
 
 