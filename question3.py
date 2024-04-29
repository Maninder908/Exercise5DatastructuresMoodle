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

    def _detach_node(self, node_to_detach):
        """Detach a node from the BST."""
        if node_to_detach is None:
            return

        # Case 1: Node has no children (leaf node)
        if node_to_detach.left is None and node_to_detach.right is None:
            self._detach_leaf(node_to_detach)
        # Case 2: Node has only one child
        elif node_to_detach.left is None or node_to_detach.right is None:
            self._detach_with_single_child(node_to_detach)
        # Case 3: Node has two children
        else:
            self._detach_with_two_children(node_to_detach)

    def _detach_with_two_children(self, node_to_detach):
        """Detach a node with two children."""
        # Find the inorder successor (the smallest node in the right subtree)
        successor_parent = node_to_detach
        successor = node_to_detach.right
        while successor.left:
            successor_parent = successor
            successor = successor.left

        # Detach the successor from its parent
        if successor_parent != node_to_detach:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right

        # Replace the node to detach with the successor
        if node_to_detach != self.root:
            parent = self._find_parent(node_to_detach)
            if parent.left == node_to_detach:
                parent.left = successor
            else:
                parent.right = successor
        else:
            self.root = successor

        # Update successor's left and right children
        successor.left = node_to_detach.left
        successor.right = node_to_detach.right