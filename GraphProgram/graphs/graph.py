from random import *
import scipy.special

class Graph:
    graph = []

    def print(self):
        for i in range(0, len(self.graph)):
            print(self.graph[i])

    def averagePathSize(self, size):
        sum = 0
        for i in range(0, size):
            randomA = randint(0, len(self.graph))
            randomB = randint(0, len(self.graph))
            while randomA == randomB:
                randomB = random.randint(0, len(self.graph))

            breadSearchResult = self.breadthFirstSearch(randomA, randomB)
            if breadSearchResult > 0:
                sum += breadSearchResult
        print(sum/size)
        return sum/size

    def breadthFirstSearch(self, start, goal):
        explored = []
        queue = [[start]]

        if start == goal:
            return -1
        while queue:
            path = queue.pop()
            node = path[-1]

            if node not in explored:
                neighbours = self.graph[node]
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == goal:
                        return len(new_path)

                explored.append(node)
        return -1

    def clusteringCoeffizient(self):
        for i in range(0, len(self.graph)):
            neighbours = self.graph[i]
            grade = len(neighbours)
            possibleEdges = scipy.special.binom(grade, 2)
            actualEdges = 0
            for neighbour in neighbours:
                self.graph[neighbour]
