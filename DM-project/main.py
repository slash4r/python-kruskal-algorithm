from Kruskal import MSTKruskal, Graph, visualize_solution

g = Graph().generate_random_graph(50, 0.4)

mst_edges = MSTKruskal(g).kruskal_mst(print_info=True, return_info=False, use_matrix=True)
mst_edges = MSTKruskal(g).kruskal_mst(print_info=True, return_info=False, use_matrix=False)
visualize_solution(g, mst_edges)
