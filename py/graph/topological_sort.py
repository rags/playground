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


############################## TESTS ##############################
import pytest

def should_topt_sort():
    assert [3,  5,  7,  8,  11,  2,  9,  10] == topological_sort(
        {
            7: [8, 11],
            11:  [2, 9, 10],
            5:  [11],
            3:  [10, 8],
            8: [9],
            2: [],
            9: [],
            10: [] })
    assert [4, 5, 6, 0, 2, 3, 1] == topological_sort(
        {
            0: [],
            1:  [],
            2:  [3],
            3:  [1],
            4: [0, 1],
            5: [0, 2],
            6: [],
            })

    assert ['B', 'A', 'D', 'C', 'E'] == topological_sort(
        {
            'A': ['C', 'D'],
            'B':  ['A', 'D'],
            'C':  ['E'],
            'D':  ['C', 'E'],
            'E': [],
          })
    assert ['B', 'A', 'D', 'C', 'E'] == topological_sort(
        {
            'A': ['C', 'D'],
            'B':  ['A', 'D'],
            'C':  ['E'],
            'D':  ['C', 'E'],
            'E': [],
          })

    assert ['S', 'A', 'B', 'C', 'E', 'D', 'G', 'F', 'T'] == topological_sort(
        {'S': {'A': 1, 'B': 9},
         'A': {'C': 3, 'D': 1},
         'B': {'D': 1, 'E': 2},
         'C': {'F': 2},
         'D': {'F': 7, 'G': 8},
         'E': {'G': 3},
         'F': {'T': 5},
         'G': {'T': 2},
         'T': {}})
    
    with pytest.raises(AssertionError) as e:
        topological_sort({1: [2], 2: [3], 3: [1]})
    assert "Cycles in graph?" == str(e.value)
    
    with pytest.raises(AssertionError) as e:
        topological_sort({0: [1], 1: [2], 2: [3], 3: [1]})
    assert "Cycles in graph?" == str(e.value)



