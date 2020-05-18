from graphs.graph import Graph
from random import *

class WattsStrogatzGraph(Graph):

    def __init__(self, n, p, k):
        for i in range(0, n):
            self.graph.insert(i, [])
        for i in range(0, n):
            for j in range(0, k):
                random = randint(0, 100000)
                if random < p * 100000:
                    self.graph[i].append(randint(0,n - 1))
                else:
                    self.graph[i].append((i + j) % n)
        print(self.graph)