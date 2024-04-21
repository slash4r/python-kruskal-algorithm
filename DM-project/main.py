from Kruskal import MSTKruskal, Graph, visualize_solution

g = Graph().generate_random_graph(20, 0.4)

mst_edges = MSTKruskal(g).kruskal_mst(print_info=True, return_info=False)
visualize_solution(g, mst_edges)
