from graphs.graph import Graph


class WattsStrogatzGraph(Graph):

    def __init__(self, n, p, k):
        for i in range(0, n):
            self.graph.insert(i, [])
        for i in range(0, n):
            for j in range(0, k):
                self.graph[i].append((i + j) % n)
        print(self.graph)