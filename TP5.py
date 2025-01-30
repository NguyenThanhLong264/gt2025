import heapq
import numpy as np

# Construct Adjacency Matrix
# --------------------------------------------------------------------------------
num_nodes = len(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M'])
node_index_map = {node: idx for idx, node in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M'])}
adj_matrix = [[float('inf')] * num_nodes for _ in range(num_nodes)]
edges = [
    ('A', 'C', 1), ('A', 'B', 4),
    ('B', 'F', 3),
    ('C', 'D', 8), ('C', 'F', 7),
    ('D', 'H', 5),
    ('F', 'H', 1), ('F', 'E', 1),
    ('E', 'H', 2),
    ('H', 'G', 3), ('H', 'M', 7), ('H', 'L', 6),
    ('G', 'M', 4),
    ('M', 'L', 1),
    ('L', 'G', 4), ('L', 'E', 2)
]

for u, v, w in edges:
    start_idx, end_idx = node_index_map[u], node_index_map[v]
    adj_matrix[start_idx][end_idx] = w
    adj_matrix[end_idx][start_idx] = w

adj_matrix_np = np.array(adj_matrix)

def format_value(value):
    return " inf" if value == float('inf') else f"{int(value):4d}"

formatted_matrix = np.array2string(
    adj_matrix_np,
    formatter={"all": format_value},
    separator=" ",
    max_line_width=120
)
print("Adjacency Matrix (Undirected Weighted Graph):")
print(formatted_matrix)
# --------------------------------------------------------------------------------

# Map indices back to nodes
index_to_node = {idx: node for node, idx in node_index_map.items()}

# Find Shortest Path
# --------------------------------------------------------------------------------
def find_shortest_path(adj_matrix, start, end):
    start_idx = node_index_map[start]
    end_idx = node_index_map[end]
    
    distances = [float('inf')] * num_nodes
    distances[start_idx] = 0
    previous_nodes = [None] * num_nodes
    priority_queue = [(0, start_idx)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor_idx, weight in enumerate(adj_matrix[current_node]):
            if weight != float('inf'):
                new_distance = current_distance + weight
                if new_distance < distances[neighbor_idx]:
                    distances[neighbor_idx] = new_distance
                    previous_nodes[neighbor_idx] = current_node
                    heapq.heappush(priority_queue, (new_distance, neighbor_idx))
    
    path = []
    current = end_idx
    while current is not None:
        path.append(index_to_node[current])
        current = previous_nodes[current]
    path.reverse()
    return path, distances[end_idx]

# Input and Output
# --------------------------------------------------------------------------------
start_node = input("Enter source node (A-M): ").strip().upper()
end_node = input("Enter target node (A-M): ").strip().upper()

if start_node in node_index_map and end_node in node_index_map:
    path, total_weight = find_shortest_path(adj_matrix, start_node, end_node)
    print(f"Shortest path from {start_node} to {end_node}: {' -> '.join(path)}")
    print(f"Total path weight: {total_weight}")
else:
    print("Invalid input. Please use valid node labels (A-M).")
# --------------------------------------------------------------------------------