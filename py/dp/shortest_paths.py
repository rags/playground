#Find shortest distances from every node to every other node in a graph
import numpy as np

def make_matrix_rep(graph):
    n = len(graph)
    matrix =  np.zeros((n, n)) + np.inf # n*n matrix with infinite distances
    matrix[np.diag_indices(n)] = 0 # and 0 distance along diag
    indices = dict(zip(graph.keys(), range(len(graph))))
    for node, neighbors in graph.items():
        i = indices[node]
        for neighbor, distance in neighbors.items():
            matrix[i][indices[neighbor]] = distance
    return matrix, indices

def make_graph_rep(matrix, nodes):
    index_to_nodes = dict(zip(nodes.values(), nodes.keys()))
    return { src: {dest: (matrix[nodes[src]][nodes[dest]][0],
                          index_to_nodes[matrix[nodes[src]][nodes[dest]][1]])
                   for dest in nodes}
             for src in nodes}

def shortest_distances_n3logn(graph):
    matrix, nodes = make_matrix_rep(graph) #O(n^2)
    indices = nodes.values()
    shortest = [[ (val, i) for val in row] for i, row in enumerate(matrix)] #O(n^2)
    # Total O(n^3log(n))
    # ceil(logn) - The repeated doubling process should exceed n.
    # So for n=38, you go upto 64. Results for shortest paths do not change after (n-1)
    # ceil(log 38) = 6; 2^6= 64
    for i in range(int(np.ceil(np.log2(len(nodes))))):  #O(log(n))
        new_shortest = np.copy(shortest)
        for src in indices: #O(n)
            for via in indices: #O(n)
                for dest in indices: #O(n)
                    new_dist = shortest[src][via][0] + shortest[via][dest][0]
                    if new_dist < shortest[src][dest][0]:
                        shortest[src][dest] = (new_dist, shortest[via][dest][1])
    return (shortest, nodes)

def min_route(*args):
    min_ = args[0]
    for arg in args[1:]:
        if arg[0] < min_[0]:
            min_ = arg
    return min_
#complexity = O(n^2) + O(n^2) + O(n^4) + O(n^2) = O(n^4)
def shortest_distances_n4(graph):
    matrix, nodes = make_matrix_rep(graph) #O(n^2)
    indices = nodes.values()
    shortest = [[ (val, i) for val in row] for i, row in enumerate(matrix)] #O(n^2)
    
    # Total O(n^4)
    # add one more edge at a time
    for i in indices:  #O(n)
        new_shortest = np.copy(shortest)
        for src in indices: #O(n)
            for via in indices: #O(n)
                for dest in indices: #O(n)
                    new_dist = shortest[src][via][0] + matrix[via][dest]
                    new_shortest[src][dest] = min_route(tuple(shortest[src][dest]),
                                                        tuple(new_shortest[src][dest]),
                                                        (new_dist, via))
        shortest = new_shortest
    return (shortest, nodes)

#floyd-warshall
def shortest_distances_n3(graph):
    matrix, nodes = make_matrix_rep(graph) #O(n^2)
    indices = nodes.values()
    shortest = [[ (val, i) for val in row] for i, row in enumerate(matrix)] #O(n^2)
    
    # Total O(n^3)
    for via in indices: #O(n)
        for src in indices: #O(n)
            for dest in indices: #O(n)
                new_dist = shortest[src][via][0] + shortest[via][dest][0]
                if new_dist < shortest[src][dest][0]:
                    shortest[src][dest] = (new_dist, shortest[via][dest][1])
    return (shortest, nodes)



############################## TESTS ##############################
    
import pytest
@pytest.mark.parametrize(('algorithm'),[shortest_distances_n4, shortest_distances_n3logn, shortest_distances_n3])
@pytest.mark.parametrize(('graph', 'shortest_paths'),
                        [({'A': {'B': 3, 'C': 8, 'E': -4},
                           'B': {'D': 1, 'E': 7},
                           'C': {'B': 4},
                           'D': {'C': -5, 'A': 2},
                           'E': {'D': 6}},
                          {'A': {'A': (0, 'A'), 'B': (1, 'C'), 'C': (-3, 'D'),
                                 'D': (2, 'E'), 'E': (-4, 'A')},
                           'B': {'A': (3, 'D'), 'B': (0, 'B'), 'C': (-4, 'D'),
                                 'D': (1, 'B'), 'E': (-1, 'A')},
                           'C': {'A': (7, 'D'), 'B': (4, 'C'), 'C': (0, 'C'),
                                 'D': (5, 'B'), 'E': (3, 'A')},
                           'D': {'A': (2, 'D'), 'B': (-1, 'C'), 'C': (-5, 'D'),
                                 'D': (0, 'D'), 'E': (-2, 'A')},
                           'E': {'A': (8, 'D'), 'B': (5, 'C'), 'C': (1, 'D'),
                                 'D': (6, 'E'), 'E': (0, 'E')}}),
                         ({1: {5: -1},
                           2: {1: 1, 4: 2},
                           3: {2: 2, 6: -8},
                           4: {1: -4, 5: 3},
                           5: {2: 7},
                           6: {2: 5, 3: 10}},
                          {1: {1: (0, 1), 2: (6, 5), 3: (np.inf, 1),
                               4: (8, 2), 5: (-1, 1), 6: (np.inf, 1)},
                           2: {1: (-2, 4), 2: (0, 2), 3: (np.inf, 2),
                               4: (2, 2), 5: (-3, 1), 6: (np.inf, 2)},
                           3: {1: (-5, 4), 2: (-3, 6), 3: (0, 3),
                               4: (-1, 2), 5: (-6, 1), 6: (-8, 3)},
                           4: {1: (-4, 4), 2: (2, 5), 3: (np.inf, 4),
                               4: (0, 4), 5: (-5, 1), 6: (np.inf, 4)},
                           5: {1: (5, 4), 2: (7, 5), 3: (np.inf, 5),
                               4: (9, 2), 5: (0, 5), 6: (np.inf, 5)},
                           6: {1: (3, 4), 2: (5, 6), 3: (10, 6),
                               4: (7, 2), 5: (2, 1), 6: (0, 6)}})
                     ])
def should_find_shortest(graph, shortest_paths, algorithm):
    assert shortest_paths == make_graph_rep(*algorithm(graph))
    