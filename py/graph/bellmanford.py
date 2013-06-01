#An optimized version of bellamn ford
def shortest_paths(graph, source):
    queue = [source]

    #dest: (distance,parent)
    shortest = {source: (0, None)}
    no_of_nodes = len(graph)
    levels_expanded = 0
    cur_level_counter = 1
    next_level_counter = 0
    while queue and levels_expanded < no_of_nodes:
        node = queue.pop(0)
        cur_level_counter -= 1
        for neighbor, distance in graph[node].items():
            dist_via_node = shortest[node][0] + distance
            if (not neighbor in shortest or
                shortest[neighbor][0] > dist_via_node):
                if neighbor not in queue:
                    queue.append(neighbor)
                    next_level_counter += 1
                shortest[neighbor] = (dist_via_node, node)

        if cur_level_counter == 0:
            levels_expanded += 1
            cur_level_counter, next_level_counter = next_level_counter, 0
            #print queue, shortest, levels_expanded, cur_level_counter, next_level_counter

    assert len(queue) == 0, "Negative weight cycles in graph"
    return shortest


def bellmanford(graph, source):
    shortest = {source: (0, None)}

    for i in range(len(graph) - 1):
        for node, neighbors in graph.items():
            if not node in shortest:
                continue
            for neighbor, distance in neighbors.items():
                dist_via_node = shortest[node][0] + distance
                if (not neighbor in shortest or
                    shortest[neighbor][0] > dist_via_node):
                    shortest[neighbor] = (dist_via_node, node)

    for node, neighbors in graph.items():
        if not node in shortest:
            continue
        for neighbor, distance in neighbors.items():
            dist_via_node = shortest[node][0] + distance
#            print neighbor, shortest[neighbor][0], (dist_via_node,  node), shortest[neighbor][0] <= dist_via_node
            assert (neighbor in shortest and
                    shortest[neighbor][0] <= dist_via_node),\
                    "Negative weight cycles in graph"
    return shortest
                

                
############################## TESTS ##############################
import pytest

@pytest.mark.parametrize(('algorithm'), [shortest_paths, bellmanford])
@pytest.mark.parametrize(("graph", 'source', "distances"), [(
#            C            
#         3/   \2       
#         A      F      
#      1/   \1 /7 \5    
#     S       D    T    
#      9\  //1 \8 /2   
#         B      G      
#         2\   /3       
#            E          
{'S': {'A': 1, 'B': 9}, 'A': {'C': 3, 'D': 1},
 'B': {'D': 1, 'E': 2}, 'C': {'F': 2},
 'D': {'F': 7, 'G': 8, 'B': 1},
 'E': {'G': 3}, 'F': {'T': 5}, 'G': {'T': 2}, 'T': {}}, 'S', 
{'S': (0, None), 'A': (1, 'S'), 'B': (3, 'D'), 'C': (4, 'A'), 
 'D': (2, 'A'), 'E': (5, 'B'), 'F': (6, 'C'), 'G': (8, 'E'), 
 'T': (10, 'G')}    
),
({1: {2: 1, 6: 2}, 2: {3: 3}, 3: {4: 2}, 4: {5: 2},
  5: {2: -6, 3: -4}, 6: {2: -2, 5: 3}}, 1,
 {1: (0, None), 2: (-1, 5), 3: (1, 5),
  4: (3, 3), 5: (5, 6), 6: (2, 1)}),
                                                            
({1: {2: 1, 6: 2}, 2: {3: 3}, 3: {4: 2}, 4: {5: 2},
  5: {2: -6, 3: -4}, 6: {2: -2, 5: 3}}, 2,
 {2: (0, None), 3: (3, 2),
  4: (5, 3), 5: (7, 4)}),
                                                            
({1: {2: -3}, 2: {3: 1}, 3: {4: 1}, 4: {5: 1}, 5: {}}, 1,
 {1:(0, None), 2: (-3, 1), 3: (-2, 2), 4: (-1, 3), 5: (0, 4)}),

({'a': {'b': -1, 'c': 4}, 'b': {'c': 3, 'd': 2, 'e': 2},
  'c': {}, 'd': {'b': 1, 'c': 5}, 'e': {'d': -3}}, 'a',
 {'a': (0, None), 'b': (-1, 'a'), 'c': (2, 'b'),
  'd': (-2, 'e'), 'e': (1, 'b')}),
                                                            
#negative weight cycle                                                        
({1: {2: 1, 6: 2}, 2: {3: 3}, 3: {4: 2}, 4: {5: 1},
  5: {2: -6, 3: -4}, 6: {2: -2, 5: 3}}, 1, None)])

def should_find_shortest(graph, source, distances, algorithm):
    if distances:
        assert distances == algorithm(graph, source)
        return
    with pytest.raises(AssertionError) as e:
        algorithm(graph, source)
    assert "Negative weight cycles in graph" == str(e.value)
                
