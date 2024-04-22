import math
import time
from typing import List, Tuple

from myGraph import Graph, plt
from Heap import PriorityQueue


class UnionFind:
    """Union-Find (Disjoint Set) data structure with path compression and union_groups by rank."""

    def __init__(self):
        self.parent = {}

    def find_root(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find_root(self.parent[u])  # path compression
        return self.parent[u]

    def union_groups(self, u: int, v: int) -> None:
        root_u = self.find_root(u)
        root_v = self.find_root(v)
        self.parent[root_v] = root_u


class MSTKruskal:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.count_operations = 0.0

    def kruskal_mst(self, print_info=False, return_info=False, use_matrix=False) -> \
                                     (tuple[list[tuple[int, int, float]], float, float] | list[tuple[int, int, float]]):
        start_time = time.time() * 1000

        if use_matrix:
            sorted_edges_list = self.get_sorted_edges_matrix()
        else:
            sorted_edges_list = self.get_sorted_edges()

        e = len(sorted_edges_list.queue)
        self.count_operations = math.log(e, 2)  # nlog(n) if was array, but we have PQ with log(n)

        uf = UnionFind()
        mst_edges = []

        # initialize data structure
        for node_name in self.graph.nodes_dict:  # name -> str
            uf.parent[node_name] = node_name
            self.count_operations += 1

        while not sorted_edges_list.is_empty():
            edge = sorted_edges_list.pop()
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
            text_result = "\nSTARTING Kruskal's algorithm\nMinimum Spanning Tree (Kruskal's Algorithm):\n"
            for edge in mst_edges:
                v = edge[0]
                u = edge[1]
                w = edge[2]

                text_result += f"{v} -- {u} : {w}\n"

            print(text_result)
            print(f"Kruskal's algorithm execution time: {execution_time:.6f} ms")
            print(f"Number of operations: {int(self.count_operations)} (approximately)")

        if return_info:
            return mst_edges, execution_time, int(self.count_operations)
        return mst_edges

    def get_sorted_edges(self) -> PriorityQueue:
        edges = PriorityQueue()

        for node_name, node in self.graph.nodes_dict.items():
            for neighbor, weight in node.neighbors:
                edges.push((node_name, neighbor.name, weight), weight)

        # sort edges based on weight (3 element in tuple)
        # edges.sort(key=lambda x: x[2])
        return edges

    def get_sorted_edges_matrix(self) -> PriorityQueue:
        edges = PriorityQueue()

        for i in range(self.graph.nodes_count):
            for j in range(i + 1, self.graph.nodes_count):  # upper triangle of adjacency matrix
                if self.graph.adjacency_matrix[i][j]:  # non-empty
                    node_i = i + 1
                    node_j = j + 1
                    weight = self.graph.adjacency_matrix[i][j]  # random weight between
                    edges.push((node_i, node_j, weight), weight)
        return edges


def visualize_solution(graph: Graph, mst_edges: List[tuple[int, int, float]]):
    # original graph
    original_pos = graph.plot_graph(title='Original Graph')

    mst_g = Graph(graph.nodes_count)  # to build normal adjacency matrix

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

    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)

    g.add_edge(1, 2, 2.5)
    g.add_edge(2, 3, 1.8)
    g.add_edge(3, 1, 3.2)
    g.add_edge(2, 4, 2.0)
    g.add_edge(3, 4, 2.5)

    # Find MST
    mst_kruskal = MSTKruskal(g)
    result = mst_kruskal.kruskal_mst(print_info=True, return_info=False, use_matrix=True)
    result = mst_kruskal.kruskal_mst(print_info=True, return_info=False, use_matrix=False)
    # visualize_solution(g, result)


if __name__ == '__main__':
    main()
