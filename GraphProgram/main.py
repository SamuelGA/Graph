
from graphs.gilbert_graph import GilbertGraph
from graphs.watts_strogatz_graph import WattsStrogatzGraph
from plotter.plot import Plotter



plotter = Plotter()

gilbert = GilbertGraph(100, 0.999)
print(gilbert.clustering_coefficient())
plotter.plot_network(gilbert.graph)









