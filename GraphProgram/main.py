
from graphs.gilbert_graph import GilbertGraph
from plotter.plot import Plotter

results = []

gilbert = GilbertGraph(100, 0.05)
print(gilbert.graph)
print(gilbert.average_grade())
plotter = Plotter()
plotter.plot_network(gilbert.graph)










