import math
import time
from typing import List, Tuple

from myGraph import Graph, plt


class UnionFind:
    """Union-Find (Disjoint Set) data structure with path compression and union_groups by rank."""

    def __init__(self):
        self.parent = {}

    def find_root(self, u: str) -> str:
        if self.parent[u] != u:
            self.parent[u] = self.find_root(self.parent[u])  # path compression
        return self.parent[u]

    def union_groups(self, u: str, v: str) -> None:
        root_u = self.find_root(u)
        root_v = self.find_root(v)
        self.parent[root_v] = root_u


class MSTKruskal:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.count_operations = 0.0

    def kruskal_mst(self, print_info=False, return_info=False) -> tuple[list[tuple[str, str, float]], float, float] | \
                                                                  list[tuple[str, str, float]]:
        start_time = time.time() * 1000

        sorted_edges_list = self.get_sorted_edges()
        e = len(sorted_edges_list)
        self.count_operations = e * math.log(e, 2)

        uf = UnionFind()
        mst_edges = []

        # initialize data structure
        for node_name in self.graph.nodes_dict:  # name -> str
            uf.parent[node_name] = node_name
            self.count_operations += 1

        for edge in sorted_edges_list:
            u, v, weight = edge
            self.count_operations += 1  # check each edge
            if uf.find_root(u) != uf.find_root(v):  # not in the same group
                uf.union_groups(u, v)
                mst_edges.append((u, v, weight))
                self.count_operations += 1  # union if all ok

        # calculate execution time
        end_time = time.time() * 1000
        execution_time = end_time - start_time

        if print_info:
            text_result = "Minimum Spanning Tree (Kruskal's Algorithm):\n"
            for edge in mst_edges:
                v = edge[0]
                u = edge[1]
                w = edge[2]

                text_result += f"{v} -- {u} : {w}\n"

            print(text_result)
            print(f"Kruskal's algorithm execution time: {execution_time:.6f} ms")
            print(f"Number of operations: {int(self.count_operations)}")

        if return_info:
            return mst_edges, execution_time, self.count_operations
        return mst_edges

    def get_sorted_edges(self) -> List[Tuple[str, str, float]]:
        edges = []

        for node_name, node in self.graph.nodes_dict.items():
            for neighbor, weight in node.neighbors:
                edges.append((node_name, neighbor.name, weight))

        # sort edges based on weight (3 element in tuple)
        edges.sort(key=lambda x: x[2])
        return edges


def visualize_solution(graph: Graph, mst_edges: List[tuple[str, str, float]]):

    # original graph
    original_pos = graph.plot_graph(title='Original Graph')

    mst_g = Graph()

    for edge in mst_edges:
        v = edge[0]
        u = edge[1]
        w = edge[2]

        mst_g.add_node(v)
        mst_g.add_node(u)
        mst_g.add_edge(v, u, w)

        plt.pause(1)
        mst_g.plot_graph(original_pos, title='Copied Graph (No Edges)', v_color="#FF3131", e_color="#7DF848")
    plt.show()


def main():
    # simple example:
    g = Graph()

    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')

    g.add_edge('A', 'B', 2.5)
    g.add_edge('B', 'C', 1.8)
    g.add_edge('C', 'A', 3.2)
    g.add_edge('B', 'D', 2.0)
    g.add_edge('C', 'D', 2.5)

    # Find MST
    mst_kruskal = MSTKruskal(g)
    mst_edges = mst_kruskal.kruskal_mst()


if __name__ == '__main__':
    main()
