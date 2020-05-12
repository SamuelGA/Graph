
from graphs.gilbert_graph import GilbertGraph
from plotter.plot import Plotter

gilbert = GilbertGraph(1000, 0.04)
print(gilbert.graph)
print(gilbert.average_grade())
print(gilbert.averagePathSize(100))
print(gilbert.clustering_coefficient())

plotter = Plotter()
plotter.plot_network(gilbert.graph)









