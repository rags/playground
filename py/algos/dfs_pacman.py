import fileinput
from collections import namedtuple, deque
#from functools import map

Pos = namedtuple('Pos', ['i', 'j'])
class Pacman:
    def __init__(self, matrix, pac_pos, food_pos, bounds):
        self.matrix = matrix
        self.expanded=[]
        self.pac_pos = pac_pos
        self.food_pos = food_pos
        self.bounds = bounds
        self.q = deque()
        self.q.append(pac_pos)
        self.neighbors = [Pos(-1,0), Pos(0,-1), Pos(0,1), Pos(1,0)]
        self.visited = set()

    def add_neighbors(self, pos):
        for delta in self.neighbors:
            neighbor = Pos(pos.i + delta.i, pos.j+delta.j)
            if (0<=neighbor.i<self.bounds.i and 
                0<=neighbor.j<self.bounds.j and
                self.matrix[neighbor.i][neighbor.j] != '%'):
                self.q.append(neighbor)

    def found(self, cell):
        print(len(self.expanded))
        for c in self.expanded:
            print("{} {}".format(*c))
        print("{} {}".format(*cell))

    def bfs(self):
        while self.q:
            #print(len(self.q), self.q)
            cell = self.q.popleft()
            if cell == self.food_pos:
                self.found(cell)
                break
            if cell in self.visited: continue
            self.expanded.append(cell)
            self.visited.add(cell)
            self.add_neighbors(cell)

def main():
    with fileinput.input() as input:
        pi, pj = map(int, input.readline().split(' '))
        fi, fj = map(int, input.readline().split(' '))
        m,n = map(int, input.readline().split(' '))
        matrix = [list(input.readline().strip()) for i in range(m)]
        Pacman(matrix, Pos(pi,pj), Pos(fi,fj), Pos(m,n)).bfs()

main()
