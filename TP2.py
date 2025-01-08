from collections import defaultdict, deque

def convert_edges_to_matrix(edge_list, number_node):
    adjacency_matrix = [[0] * number_node for _ in range(number_node)]
    for start, end in edge_list:
        adjacency_matrix[start - 1][end - 1] = 1
    return adjacency_matrix

def display_matrix(matrix):
    print("Adjacency Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))

def build_adjacency_list(matrix):
    adjacency_list = defaultdict(list)
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value == 1:
                adjacency_list[row_index + 1].append(col_index + 1)
    return adjacency_list

def count_weakly_connected_components(matrix):
    adjacency_list = build_adjacency_list(matrix)
    undirected_list = defaultdict(list)
    for node, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            undirected_list[node].append(neighbor)
            undirected_list[neighbor].append(node)

    visited = set()
    weakly_count = 0

    def explore_component(node):
        queue = deque([node])
        while queue:
            current = queue.popleft()
            for neighbor in undirected_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    for node in range(1, len(matrix) + 1):
        if node not in visited:
            weakly_count += 1
            visited.add(node)
            explore_component(node)

    return weakly_count

def count_strongly_connected_components(matrix):
    adjacency_list = build_adjacency_list(matrix)

    visited = set()
    finish_stack = []

    def forward_dfs(node):
        visited.add(node)
        for neighbor in adjacency_list[node]:
            if neighbor not in visited:
                forward_dfs(neighbor)
        finish_stack.append(node)

    for node in range(1, len(matrix) + 1):
        if node not in visited:
            forward_dfs(node)

    reversed_list = defaultdict(list)
    for start, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            reversed_list[neighbor].append(start)

    visited.clear()
    strongly_count = 0

    def reverse_dfs(node):
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                stack.extend(reversed_list[current])

    while finish_stack:
        node = finish_stack.pop()
        if node not in visited:
            strongly_count += 1
            reverse_dfs(node)

    return strongly_count

if __name__ == "__main__":
    edges = [
        (1, 2),
        (1, 4),
        (2, 3),
        (2, 6),
        (5, 4),
        (5, 5),
        (5, 9),
        (6, 3),
        (6, 4),
        (7, 3),
        (7, 5),
        (7, 6),
        (7, 8),
        (8, 3),
        (8, 9),
    ]
    total_nodes = 9

    graph_matrix = convert_edges_to_matrix(edges, total_nodes)

    display_matrix(graph_matrix)

    weakly_connected = count_weakly_connected_components(graph_matrix)
    strongly_connected = count_strongly_connected_components(graph_matrix)

    print(f"\nNumber of weakly connected components: {weakly_connected}")
    print(f"Number of strongly connected components: {strongly_connected}")