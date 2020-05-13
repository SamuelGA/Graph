
from graphs.gilbert_graph import GilbertGraph
from graphs.watts_strogatz_graph import WattsStrogatzGraph
from plotter.plot import Plotter



plotter = Plotter()

gilbert = GilbertGraph(5, 0.6)
plotter.plot_network(gilbert.graph)
print(gilbert.averagePathSize(10))
print(gilbert.clustering_coefficient())










