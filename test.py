import numpy as np

# Given weighted edges for the graph
edges = [
    (1, 2, 4), (1, 5, 2), 
    (2, 3, 7), (2, 6, 5), 
    (3, 4, 1), (3, 6, 8), 
    (4, 6, 6), (4, 7, 4), (4, 8, 3),
    (5, 6, 9), (5, 7, 10),
    (6, 7, 2),
    (7, 9, 8), (8, 9, 1)
]

# Extract unique nodes
unique_nodes = sorted(set(i for edge in edges for i in edge[:2]))

# Create adjacency matrix (infinity for no connection)
n = len(unique_nodes)
INF = float('inf')
adj_matrix = np.full((n, n), INF)

# Map node labels to indices
node_index = {node: idx for idx, node in enumerate(unique_nodes)}

# Fill the adjacency matrix with given weights
for src, dest, weight in edges:
    adj_matrix[node_index[src]][node_index[dest]] = weight
    adj_matrix[node_index[dest]][node_index[src]] = weight  # Undirected graph

# Print adjacency matrix
print("Adjacency Matrix:")
print(np.where(adj_matrix == INF, 0, adj_matrix))  # Show 0 instead of INF for clarity


# Prim's Algorithm
def prim_mst(start_node):
    num_nodes = len(unique_nodes)
    selected = [False] * num_nodes
    min_edge = [(INF, -1)] * num_nodes  # (weight, parent)

    start_idx = node_index[start_node]
    min_edge[start_idx] = (0, -1)  # Root has no parent

    mst_edges = []
    total_weight = 0

    for _ in range(num_nodes):
        # Select the node with the minimum edge weight that is not selected
        u = -1
        for i in range(num_nodes):
            if not selected[i] and (u == -1 or min_edge[i][0] < min_edge[u][0]):
                u = i

        if min_edge[u][0] == INF:
            print("Graph is disconnected!")
            return None, None  # Handles the case where the graph is not fully connected

        selected[u] = True

        # If not the root, add to MST
        if min_edge[u][1] != -1:
            mst_edges.append((unique_nodes[min_edge[u][1]], unique_nodes[u], float(min_edge[u][0])))
            total_weight += min_edge[u][0]

        # Update the minimum edges for adjacent vertices
        for v in range(num_nodes):
            if adj_matrix[u][v] < min_edge[v][0] and not selected[v]:
                min_edge[v] = (adj_matrix[u][v], u)

    return mst_edges, float(total_weight)
    num_nodes = len(unique_nodes)
    selected = [False] * num_nodes
    min_edge = [(INF, -1)] * num_nodes  # (weight, parent)

    start_idx = node_index[start_node]
    min_edge[start_idx] = (0, -1)  # Root has no parent

    mst_edges = []
    total_weight = 0

    for _ in range(num_nodes):
        # Select the node with the minimum edge weight
        u = min((w, i) for i, (w, _) in enumerate(min_edge) if not selected[i])[1]
        selected[u] = True

        # If not the root, add to MST
        if min_edge[u][1] != -1:
            mst_edges.append((unique_nodes[min_edge[u][1]], unique_nodes[u], min_edge[u][0]))
            total_weight += min_edge[u][0]

        # Update the minimum edges for adjacent vertices
        for v in range(num_nodes):
            if adj_matrix[u][v] < min_edge[v][0] and not selected[v]:
                min_edge[v] = (adj_matrix[u][v], u)

    return mst_edges, total_weight


# Kruskal's Algorithm
class DisjointSet:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root1 = self.find(u)
        root2 = self.find(v)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal_mst():
    mst_edges = []
    total_weight = 0
    ds = DisjointSet(unique_nodes)

    sorted_edges = sorted(edges, key=lambda x: x[2])  # Sort edges by weight

    for u, v, weight in sorted_edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst_edges.append((u, v, weight))
            total_weight += weight

    return mst_edges, total_weight


# Input from user
root_node = int(input("\nEnter root node for Prim's algorithm: "))

# Execute Prim's Algorithm
prim_result, prim_weight = prim_mst(root_node)
print("\nMinimum Spanning Tree using Prim's Algorithm:")
print(prim_result)
print("Total Weight:", prim_weight)

# Execute Kruskal's Algorithm
kruskal_result, kruskal_weight = kruskal_mst()
print("\nMinimum Spanning Tree using Kruskal's Algorithm:")
print(kruskal_result)
print("Total Weight:", kruskal_weight)
