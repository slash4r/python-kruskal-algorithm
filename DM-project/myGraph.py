from typing import Dict, List

import matplotlib.pyplot as plt
import networkx as nx
import random


class Node:
    def __init__(self, name: int):
        self.name = name
        self.neighbors = []  # adjacency list -- List<(Node, weight)>

    def add_neighbor(self, neighbor: 'Node', weight: float = 1.0) -> None:
        """Add a neighbor (connected node) to node with an optional weight."""
        if neighbor not in self.neighbors:
            self.neighbors.append((neighbor, weight))
            neighbor.neighbors.append((self, weight))  # bidirectional connection


class Graph:
    def __init__(self, count=0):
        self.nodes_dict: Dict[int, Node] = {}  # dict to store nodes (key: name, value: object Node)
        if count != 0:
            self.adjacency_matrix = [[False] * count] * count
        else:
            self.adjacency_matrix: List[List[float, bool]] = []  # adjacency matrix (contains weighs)
        self.nodes_count = count

    def add_node(self, name: int) -> None:
        """Add a node to the graph."""
        if name not in self.nodes_dict:
            self.nodes_dict[name] = Node(name)
            self.adjacency_matrix.append([False] * len(self.adjacency_matrix))  # append new row with False (no edges)
            for row in self.adjacency_matrix:
                row.append(False)
            self.nodes_count += 1

    def add_edge(self, name1: int, name2: int, weight: float = 1.0) -> None:
        """Add an edge between two nodes with an optional weight (1 by default)."""
        if name1 in self.nodes_dict and name2 in self.nodes_dict:
            node1 = self.nodes_dict[name1]
            node2 = self.nodes_dict[name2]
            node1.add_neighbor(node2, weight)
            # print(name1, name2, "test")
            self.adjacency_matrix[name1 - 1][name2 - 1] = weight
            self.adjacency_matrix[name2 - 1][name1 - 1] = weight
        else:
            print("Error! At least one of the nodes does not exist!")

    def plot_graph(self, pos=None, title: str = 'Graph Visualization', v_color: str = "#E4E0DC", e_color: str = "#5271FF") -> dict:
        """Plot the graph using networkx and matplotlib.\n
        We use here an adjacency list, we do not consider adjacency matrix though."""
        G = nx.Graph()

        # add all nodes to the networkx graph, so unconnected will be spotted
        G.add_nodes_from(self.nodes_dict.keys())

        edge_labels = {}
        for node in self.nodes_dict.values():
            for neighbor, weight in node.neighbors:
                G.add_edge(node.name, neighbor.name, weight=weight)
                edge_labels[(node.name, neighbor.name)] = f'{weight:.2f}'  # format weight for display
        if not pos:
            # Use a fixed layout for consistent node positions
            pos = nx.circular_layout(G)  # can also try other layouts like nx.circular_layout(G), spring_layout

        # Draw the graph with fixed node positions
        nx.draw(G, pos, with_labels=True, node_color=v_color, node_size=250, font_size=6.9,
                font_color='black', font_weight='bold', edge_color=e_color, linewidths=1, width=1)
        # draw edge labels
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=6)
        plt.title(title)
        return pos

    def generate_random_graph(self, size: int, density: float) -> 'Graph':
        """Generate a random graph of given size and density."""
        if len(self.nodes_dict) != 0:
            raise ValueError("Graph is not empty!")

        if size <= 0:
            raise ValueError("Graph size must be a positive integer.")

        if density < 0 or density > 1:
            raise ValueError("Density must be a float between 0.0 and 1.0")

        for i in range(size):
            node_name = i + 1  # Use integers as node names
            self.add_node(node_name)

        for i in range(size):
            for j in range(i + 1, size):  # upper triangle of adjacency matrix
                if random.random() < density:  # add edges based on density
                    node_i = i + 1
                    node_j = j + 1
                    weight = random.uniform(-5, 45)  # random weight between
                    self.add_edge(node_i, node_j, weight)
        return self


# usage
def main():
    g = Graph()

    g.add_node(1)
    g.add_node(2)
    g.add_node(3)

    g.add_edge(1, 2, 2.5)
    g.add_edge(2, 3, 1.8)
    g.add_edge(3, 1, 3.2)

    # copy  without edges
    # copied_g = g.copy_without_edges()
    copied_g = Graph()
    copied_g.add_node(2)
    copied_g.add_node(3)
    copied_g.add_edge(2, 3, 1.8)  # test

    # original graph
    original_pos = g.plot_graph(title='Original Graph')
    print('test' + str(original_pos))
    plt.pause(2)

    # graph without edges using the same node positions
    copied_g.plot_graph(original_pos, title='Copied Graph (No Edges)', v_color="#FF3131", e_color="#7DF848")

    plt.show()


if __name__ == '__main__':
    main()
