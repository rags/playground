from numpy import random as rand
def min_span(graph):
    queue = Queue()
    nodes = graph.keys() 
    node = nodes[rand.randint(0, len(nodes))]
    span_tree = {node: {}}
    
    while True:
        for neighbor in graph[node]:
            for connection, distance in graph[neighbor].items():
                if (neighbor in span_tree and connection in span_tree or
                    not ( neighbor in span_tree or connection in span_tree)):
                    continue
                child, parent = ((neighbor, connection)
                                 if connection in span_tree else
                                 (connection, neighbor))
                queue.insert_or_update_if_smaller((distance, child, parent))
        if queue.is_empty:
            break
        distance, node, parent = queue.pop()
        if not node in span_tree:
            span_tree[node] = {}
        if not parent in span_tree:
            span_tree[parent] = {}
        span_tree[parent][node] = span_tree[node][parent] = distance
    assert len(graph) == len(span_tree), "No spaning tree"
    return span_tree
                
class Queue:

    def __init__(self):
        self.q = []
        self.q_indices = {}

    @property
    def is_empty(self):
        return len(self.q) == 0
        
    def pop(self):
        self.swap(0,-1)
        val = self.q.pop()
        self.q_indices.pop(val[1])
        self.siftdown(0)
        return val

    def siftdown(self, i):
        left, right = i * 2 + 1, i * 2 + 2
        smallest = i
        if  left < len(self.q) and self.q[left] < self.q[smallest]:
            smallest = left
        if right < len(self.q) and self.q[right] < self.q[smallest]:
            smallest = right
        if smallest != i:
            self.swap(i, smallest)
            if smallest < len(self.q) // 2:
                self.siftdown(smallest)
        
    def insert_or_update_if_smaller(self, val):
        if not val[1] in self.q_indices:
            self.insert(val)
            return
        self.update_if_smaller(val)

    def update_if_smaller(self, val):
        distance, node, parent = val
        i = self.q_indices[node]
        if self.q[i][0] > distance:
            self.q[i] = val
            self.siftup(i)
        
    def insert(self, val):
        self.q.append(val)
        i = len(self.q) - 1
        self.q_indices[self.q[i][1]] = i
        self.siftup(i)

    def swap(self, i, j):
        self.q[i], self.q[j] = self.q[j], self.q[i]
        self.q_indices[self.q[i][1]], self.q_indices[self.q[j][1]]= i, j
            
    def siftup(self, i):
        if i < 1:
            return
        parent = (i - 1) // 2
        if self.q[parent] > self.q[i]:
            self.swap(i, parent)
            self.siftup(parent)
