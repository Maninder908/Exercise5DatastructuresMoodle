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

    def _find(self, value):
        """Find a node in the BST that holds the given value."""
        return self._find_recursive(self.root, value)

    def _find_recursive(self, current_node, value):
        """Helper function for recursive search."""
        # Base case: if the node is None or the value is found
        if current_node is None or current_node.value == value:
            return current_node
        # If the value is less than the current node's value, search in the left subtree
        elif value < current_node.value:
            return self._find_recursive(current_node.left, value)
        # If the value is greater than the current node's value, search in the right subtree
        else:
            return self._find_recursive(current_node.right, value)

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

# Search for a value
found_node = bst._find(7)
print(found_node)  # Output: Node(7)

# Search for a value not in the tree
not_found_node = bst._find(8)
print(not_found_node)  # Output: None
