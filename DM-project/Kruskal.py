from myGraph import Graph
from typing import List, Tuple, Dict


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

    def kruskal_mst(self) -> List[Tuple[str, str, float]]:
        sorted_edges_list = self.get_sorted_edges()
        uf = UnionFind()
        mst_edges = []

        # initialize data structure
        for node_name in self.graph.nodes_dict:  # name -> str
            uf.parent[node_name] = node_name

        for edge in sorted_edges_list:
            u, v, weight = edge

            if uf.find_root(u) != uf.find_root(v):  # not in the same group
                uf.union_groups(u, v)
                mst_edges.append((u, v, weight))

        return mst_edges

    def get_sorted_edges(self) -> List[Tuple[str, str, float]]:
        edges = []

        for node_name, node in self.graph.nodes_dict.items():
            for neighbor, weight in node.neighbors:
                edges.append((node_name, neighbor.name, weight))

        # sort edges based on weight (3 element in tuple)
        edges.sort(key=lambda x: x[2])
        return edges


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

    print("Minimum Spanning Tree (Kruskal's Algorithm):")
    for edge in mst_edges:
        print(f"{edge[0]} -- {edge[1]} : {edge[2]}")


if __name__ == '__main__':
    main()


