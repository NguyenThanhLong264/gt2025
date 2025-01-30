import heapq
import numpy as np


# Construct Adjacency Matrix
# --------------------------------------------------------------------------------
n = 9
adj_matrix = np.zeros((n, n))

edges = [
    (1, 2, 4), (1, 5, 1), (1, 7, 2),
    (2, 3, 7), (2, 6, 5),
    (3, 4, 1), (3, 6, 8),
    (4, 6, 6), (4, 7, 4), (4, 8, 3),
    (5, 6, 9), (5, 7, 10),
    (6, 9, 2),
    (7, 9, 8), 
    (8, 9, 1),
    (9,8,7)
]

for edge in edges:
    u, v, w = edge
    adj_matrix[u-1][v-1] = w
    adj_matrix[v-1][u-1] = w

print(adj_matrix)
# --------------------------------------------------------------------------------


# Prim's algo
# --------------------------------------------------------------------------------
def prim(adj_matrix, start_node):
    n = len(adj_matrix)
    visited = [False] * n
    min_heap = [(0, start_node, -1)]  # (weight, current_node, previous_node)
    mst_edges = []
    total_weight = 0

    while min_heap:
        weight, current_node, prev_node = heapq.heappop(min_heap)
        if visited[current_node]:
            continue
        visited[current_node] = True
        if prev_node != -1:
            mst_edges.append((prev_node + 1, current_node + 1, weight))
            total_weight += weight

        for neighbor in range(n):
            if adj_matrix[current_node][neighbor] != 0 and not visited[neighbor]:
                heapq.heappush(min_heap, (adj_matrix[current_node][neighbor], neighbor, current_node))

    return mst_edges, total_weight

start_node = int(input("Enter the starting node for Prim's algorithm (1-9): ")) - 1
mst_edges, total_weight = prim(adj_matrix, start_node)
print("\nMinimum Spanning Tree using Prim's Algorithm:")
for edge in mst_edges:
    print(f"Edge {edge[0]}-{edge[1]} with weight {edge[2]}")
print("Total weight of MST (Prim's):", total_weight)
# --------------------------------------------------------------------------------


# kruskal algo
# --------------------------------------------------------------------------------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(edges, n):
    uf = UnionFind(n)
    mst_edges = []
    total_weight = 0

    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((u + 1, v + 1, weight))
            total_weight += weight

    return mst_edges, total_weight

# Create the edge list
edges = []
for i in range(n):
    for j in range(i + 1, n):
        if adj_matrix[i][j] != 0:
            edges.append((i, j, adj_matrix[i][j]))

mst_edges, total_weight = kruskal(edges, n)
print("\nMinimum Spanning Tree using Kruskal's Algorithm:")
for edge in mst_edges:
    print(f"Edge {edge[0]}-{edge[1]} with weight {edge[2]}")
print("Total weight of MST (Kruskal's):", total_weight)
# --------------------------------------------------------------------------------