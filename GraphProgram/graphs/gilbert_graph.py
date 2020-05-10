from random import *
from graphs.graph import Graph


class GilbertGraph(Graph):
    def __init__(self, n, p):
        for i in range(0, n):
            self.graph.insert(i, [])
            for k in range(0, i + 1):
                x = randint(1, 100)
                if x > p * 100 or i == k:
                    self.graph[i].insert(k, 0)
                else:
                    self.graph[i].insert(k, 1)




