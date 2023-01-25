"""
1761. Minimum Degree of a Connected Trio in a Graph
You are given an undirected graph. You are given an integer n which is the number of nodes in the graph and an array edges, where each edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi.

A connected trio is a set of three nodes where there is an edge between every pair of them.

The degree of a connected trio is the number of edges where one endpoint is in the trio, and the other is not.

Return the minimum degree of a connected trio in the graph, or -1 if the graph has no connected trios.

 

Example 1:


Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
Output: 3
Explanation: There is exactly one trio, which is [1,2,3]. The edges that form its degree are bolded in the figure above.
Example 2:


Input: n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
Output: 0
Explanation: There are exactly three trios:
1) [1,4,3] with degree 0.
2) [2,5,6] with degree 2.
3) [5,6,7] with degree 2.
 

Constraints:

2 <= n <= 400
edges[i].length == 2
1 <= edges.length <= n * (n-1) / 2
1 <= ui, vi <= n
ui != vi
There are no repeated edges.
"""

# Time limit exceeded - n=15. O(n^3)
class Solution1:
    def dfs(self, node, level=0, path=[]):
        if node in path:
            if len(path)>2 and path[-3]==node:
                self.triangle_nodes.append({path[-1],path[-2], path[-3]})
            return
        if len(path) > 3: return
        path.append(node)
        for next_node in self.graph[node]:
            if (not path or next_node != path[-1]):
               self.dfs(next_node, level+1, path[:])


    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        self.graph = [set() for i in range(n+1)]
        for x,y in edges:
            self.graph[x].add(y)
            self.graph[y].add(x)
        self.triangle_nodes = []
        for i in range(1,n+1):
                self.dfs(i, 0, [])
        deg = float('inf')
        for triangle in self.triangle_nodes:
            cur_deg=0
            for node in triangle:
                cur_deg += len(self.graph[node] - triangle)
            deg = min(cur_deg, deg)
        return -1 if deg==float('inf') else deg


# Time limit exceeded - n=400, O(n*E), n=nodes, E=edges
import math
class Solution2:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        self.graph = [set() for i in range(n+1)]
        self.triangles = []
        for x,y in edges:
            common_neighbors = self.graph[x] & self.graph[y]
            for neighbor in common_neighbors:
                self.triangles.append({x,y,neighbor})
            self.graph[x].add(y)
            self.graph[y].add(x)
        deg = math.inf
        for triangle in self.triangles:
            cur_deg=0
            for node in triangle:
                cur_deg += len(self.graph[node]) - 2 # remove the 2 neighbors from triangle
            deg = min(cur_deg, deg)
        return -1 if deg is math.inf else deg



import math
class Solution3: #O(n?), N=15 TLE
    def dfs(self, node, visiting, parent=None, gp=None):
        if node in visiting: #cycle
            return
        v = None
        for neighbor in self.graph[node]:
            if neighbor == gp and self.deg>0: #triangle 
                self.deg = min(self.deg, self.degrees[node] + self.degrees[parent] + self.degrees[gp] - 6)
                continue
            if neighbor in visiting: continue
            if not v:
                v = visiting.copy()
                v.add(node)
            self.dfs(neighbor, v, node, parent)
        self.visited.add(node)
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        self.graph = [set() for i in range(n+1)]
        self.triangles = []
        for x,y in edges:
            self.graph[x].add(y)
            self.graph[y].add(x)
        print(self.graph)
        self.visited=set()
        self.deg = math.inf
        self.degrees = [len(self.graph[i]) for i in range(n+1)]
        for node in range(1,n+1):
            if node not in self.visited:
                self.dfs(node, set())
        
        return -1 if self.deg is math.inf else self.deg


import math
class Solution: #Accepted
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        self.graph = [set() for i in range(n+1)]
        self.triangles = []
        for x,y in edges:
            self.graph[x].add(y)
            self.graph[y].add(x)
        self.degrees = [len(self.graph[i])-2 for i in range(n+1)]
        self.deg = math.inf

        for a in range(1,n-1):
            for b in range(a+1,n):
                for c in range(b+1,n+1):
                    if self.deg <= 0: break
                    if a in self.graph[b] and b in self.graph[c] and c in self.graph[a]:
                        self.deg = min(self.degrees[a] + self.degrees[b] + self.degrees[c], self.deg)

        return -1 if self.deg is math.inf else self.deg

