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
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == goal:
                        return len(new_path)

                explored.append(node)
        return -1

    def clustering_coefficient(self):
        average_clustering_coefficient = 0
        n = 0
        for i in range(0, len(self.graph)):
            neighbours = self.graph[i]
            grade = len(neighbours)
            possible_edges = scipy.special.binom(grade, 2)
            actual_edges = 0
            checked_neighbours = []

            # check all neighbour connections
            for neighbour in neighbours:
                neighbours_neighbours = self.graph[neighbour].copy()

                # remove already checked neighbours
                for same_neighbour in self.intersection(neighbours_neighbours, checked_neighbours):
                    neighbours_neighbours.remove(same_neighbour)
                same_neighbours = list(set(neighbours_neighbours) & set(self.graph[i]))
                checked_neighbours.append(neighbour)
                actual_edges += len(same_neighbours)

            if actual_edges > 0:
                average_clustering_coefficient += actual_edges / possible_edges
                n += 1
        return average_clustering_coefficient / n

    # Python program to illustrate the intersection
    # of two lists in most simple way
    def intersection(self, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

        # Driver Code

