
from graphs.gilbert_graph import GilbertGraph
from graphs.watts_strogatz_graph import WattsStrogatzGraph
from plotter.plot import Plotter


gilbert = GilbertGraph(10000, 0.01)
print(gilbert.graph)
print(gilbert.average_grade())
print(gilbert.clustering_coefficient())







