from Kruskal import MSTKruskal, Graph, plt, visualize_solution


def experiment(fixed_size: int):
    avg_execution_times = []  # List to store average execution times
    avg_count_operations = []  # List to store average count of operations

    density = 0.9
    for i in range(5):
        total_execution_time = 0.0
        total_count_operations = 0

        for j in range(20):
            g = Graph().generate_random_graph(fixed_size, density)
            mst_edges2, execution_time, count_operations = MSTKruskal(g).kruskal_mst(print_info=False, return_info=True,
                                                                                     use_matrix=False)
            total_execution_time += execution_time
            total_count_operations += count_operations

        # Calculate average execution time and count of operations for this density
        avg_execution_time = total_execution_time / 20
        avg_count_ops = total_count_operations / 20

        # Store average values in lists
        avg_execution_times.append(avg_execution_time)
        avg_count_operations.append(avg_count_ops)

        density -= 0.1

    return avg_execution_times, avg_count_operations


def create_colored_table(results, headers, col_widths, color_map, use_matrix=False):
    # Prepare data for plotting
    table_data = []
    for size, (avg_exec_times, avg_count_ops) in results.items():
        for density, avg_exec_time, avg_count_op in zip([0.9, 0.8, 0.7, 0.6, 0.5], avg_exec_times, avg_count_ops):
            table_data.append([size, density, avg_exec_time, avg_count_op])

    # Define colors for specific rows based on conditions
    row_colors = []

    for row in table_data:
        size, density, avg_exec_time, avg_count_op = row

        # Get color for the current size from color_map
        if size in color_map:
            color = color_map[size]
        else:
            color = 'white'  # Default color for other sizes

        row_colors.append([color] * len(row))  # Assign the same color to all cells in the row

    # Display table using matplotlib
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.axis('tight')
    ax.axis('off')

    table = ax.table(cellText=table_data, colLabels=headers,
                     cellLoc='center', loc='center', colColours=['lightblue'] * len(headers),
                     cellColours=row_colors,
                     colWidths=col_widths)

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    title_type = 'Adjacency List'
    if use_matrix:
        title_type = 'Adjacency Matrix'
    plt.title(' ')
    plt.show()


# Example usage:
sizes = [20, 40, 60, 80, 100, 120, 140, 160, 180]
results = {size: experiment(size) for size in sizes}

headers = ["Graph Size", "Density", "Avg Execution Time (ms)", "Avg Count of Operations"]
col_widths = [0.15, 0.1, 0.25, 0.25]

# Define color map for sizes
color_map = {
    20: '#FF3131',
    40: 'orange',
    60: 'yellow',
    80: '#00CF40',
    100: '#38B6FF',
    120: '#5271FF',
    140: 'magenta',
    160: '#CB6CE6',
    180: 'white'
}

# Create and display the colored table
create_colored_table(results, headers, col_widths, color_map)

# mst_edges1 = MSTKruskal(g).kruskal_mst(print_info=True, return_info=False, use_matrix=True)
#                                               # mst_edges, execution_time, count_operations
# mst_edges2, execution_time, count_operations = MSTKruskal(g).kruskal_mst(print_info=True, return_info=True, use_matrix=False)
