class Node:
    def __init__(self, name: str):
        self.name = name
        self.neighbors = []  # adjacency list -- List<Node>

    def add_neighbor(self, neighbor: 'Node') -> None:
        """Add a neighbor (connected node) to node."""
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
            neighbor.neighbors.append(self)  # bidirectional connection
