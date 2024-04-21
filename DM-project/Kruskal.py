from myGraph import Graph, plt
from typing import List, Tuple


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

    # original graph
    original_pos = g.plot_graph(title='Original Graph')

    # Find MST
    mst_kruskal = MSTKruskal(g)
    mst_edges = mst_kruskal.kruskal_mst()

    MSTg = Graph()
    text_result = "Minimum Spanning Tree (Kruskal's Algorithm):\n"
    for edge in mst_edges:
        v = edge[0]
        u = edge[1]
        w = edge[2]

        MSTg.add_node(v)
        MSTg.add_node(u)
        MSTg.add_edge(v, u, w)

        text_result += f"{v} -- {u} : {w}\n"

        plt.pause(2)
        MSTg.plot_graph(original_pos, title='Copied Graph (No Edges)', v_color="#FF3131", e_color="#7DF848")

    print(text_result)
    plt.show()
    # print("Minimum Spanning Tree (Kruskal's Algorithm):")
    # for edge in mst_edges:
    #     print(f"{edge[0]} -- {edge[1]} : {edge[2]}")

    # # copy  without edges
    # # copied_g = g.copy_without_edges()
    # copied_g = Graph()
    # copied_g.add_node('B')
    # copied_g.add_node('C')
    # copied_g.add_edge('B', 'C', 1.8)  # test
    #
    # print('test' + str(original_pos))
    # plt.pause(2)
    #
    # # graph without edges using the same node positions
    # copied_g.plot_graph(original_pos, title='Copied Graph (No Edges)', v_color="#FF3131", e_color="#7DF848")


if __name__ == '__main__':
    main()

