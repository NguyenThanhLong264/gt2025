# A
# ----------------------------------------------------------------------------------------------------------------------------
num_nodes = 8
adj_matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]# Initialize the adjacency matrix with zeros

# Define the edges of the graph
edges = [
    (1, 2), (1, 3), 
    (2, 4), (2, 5), 
    (3, 6),         
    (4, 8),        
    (5, 7),         
    (6, 5)          
]

for edge in edges:
    start, end = edge
    adj_matrix[start-1][end-1] = 1 
    
for row in adj_matrix:
    print(row)
# ----------------------------------------------------------------------------------------------------------------------------

# B
# ----------------------------------------------------------------------------------------------------------------------------
def inOrder(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    
    # Assuming the graph is represented as an adjacency list
    children = graph.get(node, [])
    
    # Visit left child (if exists)
    if len(children) > 0:
        left_child = children[0]
        if left_child not in visited:
            inOrder(graph, left_child, visited)
    
    # Visit current node
    print(node, end=' ')
    
    # Visit right child (if exists)
    if len(children) > 1:
        right_child = children[1]
        if right_child not in visited:
            inOrder(graph, right_child, visited)
    
    # Visit remaining children (if any)
    for child in children[2:]:
        if child not in visited:
            inOrder(graph, child, visited)

# Example usage
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [8],
    5: [7],
    6: [5],
    7: [],
    8: []
}

# Input node label (x)
x = int(input("\nEnter the node label (x) for inorder traversal: "))
inOrder(graph, x)
