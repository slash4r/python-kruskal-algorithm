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
        """Add an edge between two nodes with an optional weight (1 by default)."""
        if name1 in self.nodes_dict and name2 in self.nodes_dict:
            node1 = self.nodes_dict[name1]
            node2 = self.nodes_dict[name2]
            node1.add_neighbor(node2, weight)
        else:
            print("Error! At least one of the nodes does not exist!")

    def copy_without_edges(self) -> 'Graph':
        """Create a copy of the graph without any edges (only nodes)."""
        copied_graph = Graph()
        # Add all nodes from the original graph to the copied graph
        for node_name in self.nodes_dict:
            copied_graph.add_node(node_name)
        return copied_graph

    def plot_graph(self, pos=None, title: str = 'Graph Visualization', v_color: str = "#E4E0DC", e_color: str = "#5271FF") -> dict:
        """Plot the graph using networkx and matplotlib."""
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
            pos = nx.spring_layout(G)  # can also try other layouts like nx.shell_layout(G)

        # Draw the graph with fixed node positions
        nx.draw(G, pos, with_labels=True, node_color=v_color, node_size=400, font_size=12,
                font_color='black', font_weight='bold', edge_color=e_color, linewidths=1, width=2)
        # draw edge labels
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)
        plt.title(title)
        return pos


# usage
def main():
    g = Graph()

    g.add_node('A')
    g.add_node('B')
    g.add_node('C')

    g.add_edge('A', 'B', 2.5)
    g.add_edge('B', 'C', 1.8)
    g.add_edge('C', 'A', 3.2)

    # copy  without edges
    # copied_g = g.copy_without_edges()
    copied_g = Graph()
    copied_g.add_node('B')
    copied_g.add_node('C')
    copied_g.add_edge('B', 'C', 1.8)  # test

    # original graph
    original_pos = g.plot_graph(title='Original Graph')
    print('test' + str(original_pos))
    plt.pause(2)

    # graph without edges using the same node positions
    copied_g.plot_graph(original_pos, title='Copied Graph (No Edges)', v_color="#FF3131", e_color="#7DF848")

    plt.show()


if __name__ == '__main__':
    main()
