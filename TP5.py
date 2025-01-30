import numpy as np
import heapq

# Define adjacency matrix representation for graph G
INF = float('inf')

nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L", "M"]
node_index = {nodes[i]: i for i in range(len(nodes))}

adj_matrix = np.full((len(nodes), len(nodes)), INF)

# Fill adjacency matrix with given edges and weights
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

# Populate the adjacency matrix
for u, v, w in edges:
    adj_matrix[node_index[u]][node_index[v]] = w
    adj_matrix[node_index[v]][node_index[u]] = w  # Assuming undirected graph

def dijkstra(source, target):
    n = len(nodes)
    dist = {node: INF for node in nodes}
    prev = {node: None for node in nodes}
    dist[source] = 0
    pq = [(0, source)]  # (distance, node)

    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > dist[u]:
            continue
        
        for v in nodes:
            v_index = node_index[v]
            u_index = node_index[u]
            weight = adj_matrix[u_index][v_index]
            
            if weight != INF and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    
    # Reconstruct shortest path
    path = []
    step = target
    while step is not None:
        path.append(step)
        step = prev[step]
    
    path.reverse()
    return path, dist[target]

# User Input
source = input("Enter source node: ").strip().upper()
target = input("Enter target node: ").strip().upper()

if source in nodes and target in nodes:
    shortest_path, total_weight = dijkstra(source, target)
    print("\nShortest Path:", " -> ".join(shortest_path))
    print("Total Weight:", total_weight)
else:
    print("Invalid source or target node!")
