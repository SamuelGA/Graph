from random import *
from graphs.graph import Graph
import scipy.special


class GilbertGraph(Graph):

    def __init__(self, n, p):
        for i in range(0, n):
            self.graph.insert(i, [])
        for i in range(0, n):
            for k in range(0, i):
                random_number = randint(0, 10000)
                p_scalar = p * 10000
                if p_scalar > random_number:
                    self.graph[i].append(k)
                    self.graph[k].append(i)


# fast graph generation
''' 
    def __init__(self, n, p):

        # init graph
        for i in range(0, n):
            self.graph.append([])

        # generate nodes in n
        possible_edges = (n * (n-1)) / 2
        number_nodes = int(round(p * possible_edges))
        for i in range(0, number_nodes):
            random_a = randint(0,n - 1)
            random_b = randint(0,n - 1)
            while random_a == random_b:
                random_b = randint(0, n - 1)
            if random_b not in self.graph[random_a]:
                self.graph[random_a].append(random_b)
                self.graph[random_b].append(random_a)
            else:
                i = i - 1
'''







