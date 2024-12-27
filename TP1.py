from collections import defaultdict, deque

def create_graph(edges):
    """Create a graph from a list of edges."""
    graph = defaultdict(list)
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)  # Assuming an undirected graph
    return graph

def path_exists(graph, start, end):
    """Check if a path exists between start and end nodes using BFS."""
    if start not in graph or end not in graph:
        return False

    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()

        if current == end:
            return True

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return False

def main():
    # Define the graph edges
    edges = [
        ("A", "B"),
        ("B", "C"),
        ("C", "D"),
        ("E", "F"),
    ]

    # Create the graph
    graph = create_graph(edges)

    # User input
    start = input("Enter the start node: ").strip()
    end = input("Enter the end node: ").strip()

    # Check if a path exists
    if path_exists(graph, start, end):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
