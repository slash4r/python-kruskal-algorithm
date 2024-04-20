from typing import Dict

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, name: str):
        self.name = name
        self.neighbors = []  # adjacency list -- List<(Node, weight)>

    def add_neighbor(self, neighbor: 'Node', weight: float = 1.0) -> None:
        """Add a neighbor (connected node) to node with an optional weight."""
        if neighbor not in self.neighbors:
            self.neighbors.append((neighbor, weight))
            neighbor.neighbors.append((self, weight))  # bidirectional connection


class Graph:
    def __init__(self):
        self.nodes_dict: Dict[str, Node] = {}  # dict to store nodes (key: name, value: object Node)

    def add_node(self, name: str) -> None:
        """Add a node to the graph."""
        if name not in self.nodes_dict:
            self.nodes_dict[name] = Node(name)

    def add_edge(self, name1: str, name2: str, weight: float = 1.0) -> None:
        """Add an edge between two nodes with an optional weight."""
        if name1 in self.nodes_dict and name2 in self.nodes_dict:
            node1 = self.nodes_dict[name1]
            node2 = self.nodes_dict[name2]
            node1.add_neighbor(node2, weight)

    def plot_graph(self) -> None:
        """Plot the graph using networkx and matplotlib."""
        G = nx.Graph()

        # add all nodes to the networkx graph, so unconnected will be spotted
        G.add_nodes_from(self.nodes_dict.keys())

        edge_labels = {}
        for node in self.nodes_dict.values():
            for neighbor, weight in node.neighbors:
                G.add_edge(node.name, neighbor.name, weight=weight)
                edge_labels[(node.name, neighbor.name)] = f'{weight:.2f}'  # format weight for display

        # compute node positions using a spring layout algorithm to achieve a visually appealing layout!
        pos = nx.spring_layout(G)

        # draw the graph
        nx.draw(G, pos, with_labels=True, node_color='#FF3131', node_size=400, font_size=12, font_color='black',
                font_weight='bold', edge_color='#5271FF', linewidths=1, width=2)

        # draw edge labels
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)

        plt.title('Graph Visualization')
        plt.show()


# usage
g = Graph()

g.add_node('A')
g.add_node('B')
g.add_node('C')

g.add_edge('A', 'B', 2.5)
g.add_edge('B', 'C', 1.8)
g.add_edge('C', 'A', 3.2)

g.plot_graph()
