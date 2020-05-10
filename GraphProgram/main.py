
from graphs.gilbert_graph import GilbertGraph

gilbert = GilbertGraph(1000, 0.05)

print(gilbert.averagePathSize(100))