import numpy as np

# Given edges for graph G
edges = [
    (1, 2), (1, 3), 
    (2, 4), (2, 5), 
    (3, 6),         
    (4, 8),        
    (5, 7),         
    (6, 5)          
]

# Extract unique nodes
unique_nodes = sorted(set(i for edge in edges for i in edge))

# Create adjacency matrix
n = len(unique_nodes)
node_index = {node: idx for idx, node in enumerate(unique_nodes)}
adj_matrix = np.zeros((n, n), dtype=int)

# Fill the adjacency matrix
for src, dest in edges:
    adj_matrix[node_index[src]][node_index[dest]] = 1

# Print the adjacency matrix
print("Adjacency Matrix:")
print(adj_matrix)


# Tree Structure for In-Order Traversal
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Construct tree from edges
def build_tree():
    tree_nodes = {i: TreeNode(i) for i in unique_nodes}  # Avoid variable conflict

    # Manually linking based on given edges
    tree_nodes[1].left, tree_nodes[1].right = tree_nodes.get(2), tree_nodes.get(3)
    tree_nodes[2].left, tree_nodes[2].right = tree_nodes.get(4), tree_nodes.get(5)
    tree_nodes[3].left = tree_nodes.get(6)
    tree_nodes[4].left = tree_nodes.get(8)
    tree_nodes[5].right = tree_nodes.get(7)
    tree_nodes[6].left = tree_nodes.get(5)  # Handling back edge (6,5) in a binary way

    return tree_nodes

# In-order traversal from a given node
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)

# Function to print in-order traversal for a given node
def print_inorder_subtree(start_node_label):
    tree_nodes = build_tree()
    if start_node_label in tree_nodes:
        print(f"\nIn-order Traversal from Node {start_node_label}:")
        inorder_traversal(tree_nodes[start_node_label])
    else:
        print("Node not found in tree")

# Example usage
print_inorder_subtree(2)  # Change this to any node label to start traversal
