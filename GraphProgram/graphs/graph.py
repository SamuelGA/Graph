class Graph:
    graph = []

    def print(self):
        for i in range(0, len(self.graph)):
            print(self.graph[i])

    def shortestPath(self, a, b):
        print("calculating shortest path")
        print(self.neighbors(3))

    def neighbors(self, node):
        neighbors = []
        for i in range(0, node):
            if self.graph[node][i] == 1:
                neighbors.append(i)
        for i in range(node, len(self.graph)):
            if self.graph[i][node] == 1:
                neighbors.append(i)
        return neighbors