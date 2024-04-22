class Node:
    def __init__(self, name: str):
        self.name = name
        self.neighbors = []  # adjacency list -- List<(Node, weight)>

    def add_neighbor(self, neighbor: 'Node', weight: float = 1.0) -> None:
        """Add a neighbor (connected node) to node with an optional weight."""
        if neighbor not in self.neighbors:
            self.neighbors.append((neighbor, weight))
            neighbor.neighbors.append((self, weight))  # bidirectional connection
