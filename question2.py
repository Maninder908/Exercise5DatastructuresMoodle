class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'Node({self.value})'

class BST:
    def __init__(self):
        self.root = None

    def find_maximum(self):
        """Find the node with the maximum value in the BST."""
        if self.root is None:
            return None
        current_node = self.root
        while current_node.right is not None:
            current_node = current_node.right
        return current_node

    def find_minimum(self):
        """Find the node with the minimum value in the BST."""
        if self.root is None:
            return None
        current_node = self.root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

# Example usage:
# Create a BST
bst = BST()
# Insert some values
bst.root = Node(10)
bst.root.left = Node(5)
bst.root.right = Node(15)
bst.root.left.left = Node(3)
bst.root.left.right = Node(7)
bst.root.right.left = Node(12)
bst.root.right.right = Node(20)

# Find the maximum value
max_node = bst.find_maximum()
print(max_node)  # Output: Node(20)

# Find the minimum value
min_node = bst.find_minimum()
print(min_node)  # Output: Node(3)
