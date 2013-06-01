#A modified version dijikstra
from ds.heap import Heap

def cmp_frontier(f1, f2):
    return cmp(f1[1], f2[1])

def shortest_path(graph, src, dest):
    if src == dest:
        return [src], 0
    dist = traverse(graph, Heap([([src], 0)], cmp_frontier), dest)
    if not dist:
        print "No path form %s to %s" %  (src, dest)
        return
    print "The min distance from %s to %s is %s" % (src, dest, dist)
    return dist

def traverse(graph, min_heap, dest):
    while len(min_heap) > 0:
        nodes, dist_so_far= min_heap.pop()
        print nodes, dist_so_far, min_heap.vals
        frontier = nodes[-1]
        if frontier == dest:
            return nodes, dist_so_far
        for neighbor, dist in graph[frontier].items():
            min_heap.push((nodes + [neighbor], dist_so_far + dist))
    
            
############################## TESTS ########################################

'''
         C
      3/   \2
      A      F
   1/   \1 /7 \5
  S       D    T
   9\   /1  \8 /2
      B      G
      2\   /3
         E

'''        
def graph1():
    return {'S': {'A': 1, 'B': 9},
            'A': {'C': 3, 'D': 1},
            'B': {'D': 1, 'E': 2},
            'C': {'F': 2},
            'D': {'F': 7, 'G': 8},
            'E': {'G': 3},
            'F': {'T': 5},
            'G': {'T': 2},
            'T': {}}

'''        2
         #------#
    1    v      |  6             3
 A-----> B ---> C --------> E <----- F
 ^       |  3   \           ^
 |_______|       \          | 2
    2            #---> D --#
                  3
'''
def graph_with_cycles():
    return {'A': {'B': 1},
            'B': {'A': 2, 'C': 3},
            'C': {'B': 2, 'D': 3, 'E': 6},
            'D': {'E': 2},
            'E': {},
            'F': {'E', 3}}

#dijikstra's cant handle cycles'
def xshould_find_shortest_distance_with_cycles():
    graph = graph_with_cycles()
    assert (['A', 'B', 'C', 'D', 'E'], 9) == shortest_path(graph, 'A', 'E')
    assert (['C', 'B', 'A'], 4) == shortest_path(graph, 'C', 'A')
    assert (['C', 'D', 'E'], 5) == shortest_path(graph, 'C', 'E')
    assert not shortest_path(graph, 'A', 'F')
    assert not shortest_path(graph, 'D', 'A')
    
def should_find_shortest_distance():
    graph = graph1()
    assert not shortest_path(graph, 'A', 'B')
    assert (['S'], 0) == shortest_path(graph, 'S', 'S')
    assert (['S', 'A', 'C', 'F', 'T'], 11) == shortest_path(graph, 'S', 'T')
    assert (['S', 'A', 'D', 'G'], 10) == shortest_path(graph, 'S', 'G')
    
def should_work_for_samples():
    graph1 =  {'a': {'w': 14,  'x': 7,  'y': 9},
              'b': {'w': 9, 'z': 6},
              'w': {'a': 14,  'b': 9,  'y': 2},
              'x': {'a': 7,  'y': 10,  'z': 15},
              'y': {'a': 9,  'w': 2,  'x': 10,  'z': 11},
              'z': {'b': 6, 'x': 15, 'y': 11}}
    assert (['a', 'y', 'w', 'b'],  20) == shortest_path(graph1, 'a', 'b')
