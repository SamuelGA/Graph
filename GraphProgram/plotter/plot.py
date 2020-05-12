import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import networkx as nx

class Plotter:

    def plot(self, numbers):
        labels = ['10', '100', '1000', '10000']
        men_std = [0, 0, 0, 0]
        width = 0.35  # the width of the bars: can also be len(x) sequence

        fig, ax = plt.subplots()

        ax.bar(labels, numbers, width, yerr=men_std, label='Results wit p = 0.4 / n')

        ax.set_ylabel('Average Path Size')
        ax.set_title('Network Size')
        ax.legend()

        plt.show()

    def plot_network(self, nodes):
        G = nx.Graph()
        for i in range(0, len(nodes)):
            G.add_node(i)
        for i in range(0, len(nodes)):
            for k in range(0, len(nodes[i])):
                G.add_edge(i, nodes[i][k])
        plt.subplot(121)
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()


    def plotLinear(self, numbers):
        labels = ['5000', '10000', '150000', '20000', '25000', '30000', '35000', '40000', '45000', '50000']
        men_std = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        width = 0.35  # the width of the bars: can also be len(x) sequence

        fig, ax = plt.subplots()

        ax.bar(labels, numbers, width, yerr=men_std, label='Results wit P = 4 / N')

        ax.set_ylabel('Average Length')
        ax.set_title('Network Size')
        ax.legend()

        plt.show()