#find strongly connected components in a DAG
#i.e find sub graphs where there is a path (direct/indirect)
# from every node to every other node
#This concept doesnt make sense in undirected graphs
def strongly_connected_parts(graph):
    order = []
    visited = set()
    for node in graph:
        if node not in visited:
            dfs(node, graph, order, visited)
    visited.clear()
    reverse_graph = reverse(graph)
    components = []
    for node in reversed(order):
        if node not in visited:
            component = []
            dfs(node, reverse_graph, component, visited)
            components.append(component)
    return components
        
def reverse(graph):
    reverse_graph = {}
    for node, neighbors in graph.items():
        if node not in reverse_graph:
            reverse_graph[node] = []
        for neighbor in neighbors:
            if not neighbor in reverse_graph:
                reverse_graph[neighbor] = []
            reverse_graph[neighbor].append(node)
    return reverse_graph
        
def dfs(node, graph, order, visited):
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            dfs(child, graph, order, visited)
    order.append(node)

######################################## TESTS ###################################    
import pytest

def should__reverse():
    assert set([1, 2]) == {2, 1}
def should_reverse():
    assert ({1: [2, 3, 4], 2:  [],  3:  [],  4:  []} ==
            reverse({2: [1], 3: [1], 4: [1]}))
    assert {1: [2], 2: [3], 3: [1]} == reverse({1: [3], 2: [1], 3: [2]})

@pytest.mark.parametrize(('graph', 'components'),
                         #cyclic triangle
                         [({1: [2], 2: [3], 3: [1]},
                           [[1, 2, 3]]),

                          ({1: [2], 2: [3], 3: [2]},
                           [[1], [2, 3]]),

                          #cycle square
                          ({1: [2], 2: [3], 3: [4],4: [1]}, [[1, 2, 3, 4]]),

                          #cyclic star
                          ({1: [2], 2: [3], 3: [4],4: [5], 5: [1]},
                           [[1, 2, 3, 4, 5]]), 

                          #star - one edge reversed
                          ({1: [2, 5], 2: [3], 3: [4],4: [5], 5: []},
                           [[1], [2], [3], [4], [5]]), 

                          ({1: [2], 2: [3], 3: [4, 5],4: [1, 5], 5: []},
                           [[1, 2, 3, 4], [5]]), 

                          #http://en.wikipedia.org/wiki/File:Scc.png
                          ({'a': ['b'], 'b': ['c', 'e', 'f'],
                            'c': ['d', 'g'], 'd': ['c', 'h'],
                            'e': ['a', 'f'], 'f': ['g'],
                            'g': ['f'], 'h': ['d', 'g']},
                           
                           [['a', 'b', 'e'], ['f', 'g'], ['c', 'd', 'h']])
                      ])
def should_give_strongly_connected_components(graph, components):
    assert (frozenset(map(frozenset, components)) ==
            frozenset(map(frozenset, strongly_connected_parts(graph))))
    