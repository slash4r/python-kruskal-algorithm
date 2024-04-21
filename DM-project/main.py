import random

from Kruskal import MSTKruskal, Graph, plt

# !!! put it inside the class !!!
def generate_random_graph(size: int, density: float) -> Graph():
    """Generate a random graph of given size and density."""
    if size <= 0:
        raise ValueError("Graph size must be a positive integer.")

    if density < 0 or density > 1:
        raise ValueError("Density must be a float between 0.0 and 1.0")

    result = Graph()

    for i in range(size):
        node_name = str(i)  # Use integers as node names
        result.add_node(node_name)

    # Add edges based on density
    for i in range(size):
        for j in range(i + 1, size):  # Iterate over upper triangle of adjacency matrix
            if random.random() < density:
                node_i = str(i)
                node_j = str(j)
                weight = random.uniform(1, 25)  # Generate a random weight between 0.1 and 1.0
                result.add_edge(node_i, node_j, weight)

    return result


test = generate_random_graph(20, 0.2)

# !!!!to make as a function!!!!
original_pos = test.plot_graph(title='Original Graph')

# Find MST
mst_kruskal = MSTKruskal(test)
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
