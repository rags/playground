import prim
import kruskal
import pytest

def make_undirected(graph):
    for node,neighbors in graph.items():
        for neighbor, distance in neighbors.items():
            graph[neighbor][node] = distance
    return graph

@pytest.mark.parametrize(("algorithm"), [prim.min_span, kruskal.min_span])
@pytest.mark.parametrize(("disconnected_graph"),
                         [
                             {1: {2: 1}, 2: {}, 3: {4: 1},  4: {}},
                             
                             {0: {1: 1, 2: 1}, 1: {2: 1}, 2: {},  3: {}}])
def should_fail_when_no_spaning_tree(disconnected_graph, algorithm):
    with pytest.raises(AssertionError) as e:
        algorithm(make_undirected(disconnected_graph))
    assert "No spaning tree" == str(e.value)

    


@pytest.mark.parametrize(("algorithm"), [prim.min_span, kruskal.min_span])
@pytest.mark.parametrize(("graph", "min_span_trees"), [
    (
        # 
        #          C
        #       3// \\2
        #       A      F
        #    1// \\1 /7 \5
        #   S       D     T
        #    9\  //1  \8 //2
        #       B      G
        #       2\\  //3
        #          E
        # 
        # 
        {'S': {'A': 1, 'B': 9},
         'A': {'C': 3, 'D': 1},
         'B': {'D': 1, 'E': 2},
         'C': {'F': 2},
         'D': {'F': 7, 'G': 8},
         'E': {'G': 3},
         'F': {'T': 5},
         'G': {'T': 2},
         'T': {}},
        [{'S': {'A': 1},
          'A': {'C': 3, 'D': 1},
          'B': {'E': 2, 'D': 1}, 
          'C': {'F': 2},
          'D': {}, 
          'E': {'G': 3},
          'F': {}, 
          'G': { 'T': 2},
          'T': {}}]),
    
    ({'A': {'B': 3, 'F': 2},
      'B': {'C': 17, 'D': 16},
      'C': {'D': 8, 'I': 18},
      'D': {'E': 11, 'I': 4},
      'E': {'F': 1, 'G': 6, 'H': 5, 'I': 10, },
      'F': {'G': 7},
      'G': {'H': 15},
      'H': {'J': 13, 'I': 12},
      'I': {'J': 9},
      'J': {}},
     [{'A': {'B': 3, 'F': 2},
       'B': {},
       'C': {'D': 8},
       'D': {'I': 4},
       'E': {'F': 1, 'G': 6, 'H': 5, 'I': 10, },
       'F': {},
       'G': {},
       'H': {},
       'I': {'J': 9},
       'J': {}}]),
    
    ({
        0: {1: 20, 2: 45, 9: 45},
        1: {2: 30, 4: 25, 7: 100, 9: 30},
        2: {3: 45},
        3: {4: 75, 5: 40},
        4: {5: 75, 7: 90},
        5: {6: 80, 8: 40},
        6: {7: 15},
        7: {8: 45, 9: 50},
        8: {},
        9: {}
    },
     [
         {0:  {1:  20},
          1:  {9:  30,  2:  30,  4:  25},
          2:  {3:  45},
          3:  {5:  40},
          4:  {},
          5:  {8:  40},
          6:  {7:  15},
          7:  {8:  45},
          8:  {},
          9:  {}}]),
    #equilatereral triangle of size 1
    ({0: {1: 1, 2: 1},
      1: {2: 1},
      2: {}},
     #3 possible min span tree 
     [{0: {1: 1, 2: 1},
       1: {},
       2: {}},
      
      {0: {2: 1},
       1: {2: 1},
       2: {}},
      
      {0: {1: 1},
       1: {2: 1},
       2: {}}])
])
def should_find_min_span_tree(graph, min_span_trees, algorithm):
    for i in range(3):
        assert algorithm(make_undirected(graph)) in map(make_undirected, min_span_trees)
