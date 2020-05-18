from random import *
import scipy.special

class Graph:
    graph = []


    def averagePathSize(self, size):
        sum = 0
        n = 0
        for i in range(0, size):
            randomA = randint(0, len(self.graph) - 1)
            randomB = randint(0, len(self.graph) - 1)
            while randomA == randomB:
                randomB = randint(0, len(self.graph) - 1)

            breadth_search_result = self.breadthFirstSearch(randomA, randomB)

            if breadth_search_result > 0:
                sum += breadth_search_result
                n += 1
        if n == 0:
            return 0
        return sum/n

    def average_grade(self):
        average = 0
        for node in self.graph:
            average += len(node)
        return average / len(self.graph)

    def breadthFirstSearch(self, start, goal):
        explored = []
        queue = [[start]]

        if start == goal:
            return -1
        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node not in explored:
                neighbours = self.graph[node]
                for neighbour in neighbours:
                    if neighbour == goal:
                        return len(path)
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                explored.append(node)
        return -1

    def clustering_coefficient(self):
        average_clustering_coefficient = 0
        n = 0
        for i in range(0, len(self.graph)):
            neigbours = self.graph[i]

            actual_edges = 0
            checked_neighbours = []
            for neigbour in neigbours:
                same = list(set(self.graph[neigbour]) & set(neigbours))

                # remove already checked neighbours
                for checked_neighbour in checked_neighbours:
                    if checked_neighbour in same:
                        same.remove(checked_neighbour)

                if len(same) > 0:
                    actual_edges += len(same)
                checked_neighbours.append(neigbour)

            possible_edges = scipy.special.binom(len(neigbours), 2)

            if possible_edges > 0:
                clustering_coefficient = actual_edges / possible_edges
                average_clustering_coefficient += clustering_coefficient

        average_clustering_coefficient = average_clustering_coefficient / len(self.graph)
        return average_clustering_coefficient
    # Python program to illustrate the intersection
    # of two lists in most simple way
    def intersection(self, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

        # Driver Code

