from typing import Dict
from myNode import Node

import matplotlib.pyplot as plt
import networkx as nx


class Graph:
    def __init__(self):
        self.nodes_dict: Dict[str, Node] = {}  # dict to store nodes (key: name, value: object Node)

    def add_node(self, name: str) -> None:
        """Add a node to the graph."""
        if name not in self.nodes_dict:
            self.nodes_dict[name] = Node(name)

    def add_edge(self, name1: str, name2: str) -> None:
        """Add an edge between two nodes."""
        if name1 in self.nodes_dict and name2 in self.nodes_dict:
            node1 = self.nodes_dict[name1]
            node2 = self.nodes_dict[name2]
            node1.add_neighbor(node2)

    def plot_graph(self) -> None:
        """Plot the graph using networkx and matplotlib."""
        G = nx.Graph()

        # add all nodes to the networkx graph, so unconnected will be spotted
        G.add_nodes_from(self.nodes_dict.keys())

        # add edges to the networkx graph
        for node in self.nodes_dict.values():
            for neighbor in node.neighbors:
                G.add_edge(node.name, neighbor.name)

        # compute node positions using a spring layout algorithm to achieve a visually appealing layout!
        pos = nx.spring_layout(G)

        # draw the graph
        nx.draw(G, pos, with_labels=True, node_color='#FF3131', node_size=400, font_size=12, font_color='black',
                font_weight='bold', edge_color='#5271FF', linewidths=1, width=2)

        plt.title('Graph Visualization')
        plt.show()


# usage
g = Graph()

g.add_node('A')
g.add_node('B')
g.add_node('C')

g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'A')

g.plot_graph()
