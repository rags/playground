def topological_sort(graph):
    n = len(graph)
    indegree_map = make_indegree_map(graph)
    next_nodes = [node for node in graph if not indegree_map.get(node, 0)]
    #print indegree_map, next_nodes
    ordered = []
    for i in range(n):
        assert next_nodes, "Cycles in graph?"
        node = next_nodes.pop(0)
        ordered.append(node)
        for neighbor in graph[node]:
            indegree_map[neighbor] -= 1
            if not indegree_map[neighbor]:
                next_nodes.append(neighbor)
                
    #print "A", indegree_map, next_nodes

    assert not next_nodes, "Cycles in your graph?"
    assert all([not indegree_map[node] for node in indegree_map]), "Cycles in your graph?"
    return ordered
     
def make_indegree_map(graph):
    indegree_map = {}
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            indegree_map[neighbor] = indegree_map.get(neighbor, 0) + 1
    return indegree_map


def dfs(node, graph, order, visited):
    visited.add(node)
    for child in graph[node]:
        if not child in visited:
            dfs(child, graph, order, visited)
    order.insert(0, node)

    
def topological_sort_dfs(graph):
    order = []
    visited = set()
    for node in graph:
        if not node in visited:
            dfs(node, graph, order, visited)
    return order
############################## TESTS ##############################
import pytest

@pytest.mark.parametrize(("algorithm"), [topological_sort, topological_sort_dfs])
def should_sort(algorithm):
    assert algorithm(
        {
            7: [8, 11],
            11:  [2, 9, 10],
            5:  [11],
            3:  [10, 8],
            8: [9],
            2: [],
            9: [],
            10: [] }) in ([7,  5,  11,  3,  8,  9, 10, 2],
                          [3,  5,  7,  8,  11,  2,  9,  10])
    assert algorithm(
        {
            0: [],
            1:  [],
            2:  [3],
            3:  [1],
            4: [0, 1],
            5: [0, 2],
            6: [],
            }) in ([6,  5,  4,  2,  3,  1,  0], [4, 5, 6, 0, 2, 3, 1])

    assert ['B', 'A', 'D', 'C', 'E'] == algorithm(
        {
            'A': ['C', 'D'],
            'B':  ['A', 'D'],
            'C':  ['E'],
            'D':  ['C', 'E'],
            'E': [],
          })
    assert ['B', 'A', 'D', 'C', 'E'] == algorithm(
        {
            'A': ['C', 'D'],
            'B':  ['A', 'D'],
            'C':  ['E'],
            'D':  ['C', 'E'],
            'E': [],
          })

    assert algorithm(
        {'S': {'A': 1, 'B': 9},
         'A': {'C': 3, 'D': 1},
         'B': {'D': 1, 'E': 2},
         'C': {'F': 2},
         'D': {'F': 7, 'G': 8},
         'E': {'G': 3},
         'F': {'T': 5},
         'G': {'T': 2},
         'T': {}}) in (['S', 'A', 'B', 'C', 'E', 'D', 'G', 'F', 'T'],
                       ['S', 'B', 'E', 'A', 'D', 'G', 'C', 'F', 'T'] )


def dfs_should_handle_cycles():
    #This is upsurd - cannot sort DAG with cycles
    #The return values dont make any sense
    [1, 2, 3] == topological_sort_dfs({1: [2], 2: [3], 3: [1]})
    [0, 1, 2, 3] == topological_sort_dfs({0: [1], 1: [2], 2: [3], 3: [1]})

def should_throw_error():
    with pytest.raises(AssertionError) as e:
        topological_sort({1: [2], 2: [3], 3: [1]})
    assert "Cycles in graph?" == str(e.value)
    
    with pytest.raises(AssertionError) as e:
        topological_sort({0: [1], 1: [2], 2: [3], 3: [1]})
    assert "Cycles in graph?" == str(e.value)



