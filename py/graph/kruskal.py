def min_span(graph):
    edges_sorted = sortedEdges(graph)
    union_find = UnionFind(graph)
    for edge in edges_sorted:
        union_find.add(edge)
        if union_find.size == 1:
            break
    assert union_find.size == 1,  "No spaning tree"
    return union_find.graphs[0]
    

class UnionFind(object):
    def __init__(self, graph):
        self.graphs = []
        for node in (graph or {}):
            self.graphs.append({node: {}})

    @property
    def size(self):
        return len(self.graphs)

    def add(self, (distance, src, dest)):
        src_graph = dest_graph = None
        for graph in self.graphs:
            if src in graph:
                src_graph = graph
            if dest in graph:
                dest_graph = graph
        assert src_graph
        assert dest_graph
        if src_graph == dest_graph:
            return
        self.graphs.remove(dest_graph)
        src_graph.update(dest_graph)
        src_graph[src][dest] = src_graph[dest][src] = distance
                
    
def sortedEdges(graph):
    edges = []
    for node, neighbors in graph.items():
        for neighbor, distance in neighbors.items():
            edges.append((distance,node, neighbor))
    return sorted(edges)