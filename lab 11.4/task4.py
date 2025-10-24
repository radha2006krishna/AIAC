# ============================================
# Binary Search Tree (BST) Implementation
# ============================================
class Node:
    """A node in the binary search tree.
    Attributes:
        data (int): The value stored in the node.
        left (Node): Pointer to the left child.
        right (Node): Pointer to the right child.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    """Binary Search Tree class with insert, search, and inorder traversal."""
    def __init__(self):
        self.root = None
    # ------------------------------------
    def insert(self, data):
        """Insert a new value into the BST.
        Args:
            data (int): The value to insert.
        If the tree is empty, the new node becomes the root.
        Otherwise, the value is placed recursively based on comparison.
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)
    def _insert_recursive(self, current, data):
        """Helper method to recursively find the correct position."""
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)
        # Duplicate values are ignored in this implementation
    # ------------------------------------
    def search(self, value):
        """Search for a value in the BST.
        Args:
            value (int): The value to search for.
        Returns:
            bool: True if found, False otherwise.
        """
        return self._search_recursive(self.root, value)
    def _search_recursive(self, current, value):
        """Helper recursive search method."""
        if current is None:
            return False
        if current.data == value:
            return True
        elif value < current.data:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)
    # ------------------------------------
    def inorder_traversal(self):
        """Perform an inorder traversal of the BST.
        Returns:
            list: The elements of the BST in sorted order.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    def _inorder_recursive(self, current, result):
        """Helper method for inorder traversal."""
        if current:
            self._inorder_recursive(current.left, result)
            result.append(current.data)
            self._inorder_recursive(current.right, result)
# ------------------------------------
# Example Usage / Testing
# ------------------------------------
if __name__ == "__main__":
    bst = BST()
    numbers = [50, 30, 70, 20, 40, 60, 80]
    print("Inserting values into BST:", numbers)
    for num in numbers:
        bst.insert(num)
    print("\nInorder Traversal (should be sorted):")
    print(bst.inorder_traversal())  # Expected: [20, 30, 40, 50, 60, 70, 80]
    # Test search
    present = 60
    absent = 100
    print(f"\nSearch {present}: {bst.search(present)}  (Expected: True)")
    print(f"Search {absent}: {bst.search(absent)}  (Expected: False)")
