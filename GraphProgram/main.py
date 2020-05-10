
from graphs.gilbert_graph import GilbertGraph

gilbert = GilbertGraph(10, 0.6)

gilbert.print()

gilbert.shortestPath(3, 2)