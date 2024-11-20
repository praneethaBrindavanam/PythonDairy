A tree is a hierarchical data structure consisting of nodes. The topmost node is the root, and each node may have child nodes. Trees are commonly used in scenarios where data needs to be represented hierarchically, such as file systems, organizational structures, and more.

Terminology:
Root: The topmost node.
Parent/Child: Nodes are connected; the higher node is the parent, and the lower one is the child.
Leaf: A node with no children.
Depth: The level of a node in the tree.
Height: The longest path from a node to its leaf.

  Binary Tree
A binary tree is a tree where each node has at most two children, referred to as the left and right child.

Example of a Binary Tree





Python Implementation:
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Example Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Traversing the Tree (Preorder)
def preorder_traversal(node):
    if node:
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

preorder_traversal(root)  # Output: 1 2 4 5 3





Binary Search Tree (BST)
A binary search tree (BST) is a special type of binary tree where:

The value of each node in the left subtree is less than the node.
The value of each node in the right subtree is greater than the node.
Example of a Binary Search Tree





Python Implementation:
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = BSTNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = BSTNode(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = BSTNode(value)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

# Example Usage
bst = BST()
values = [10, 5, 15, 2, 7, 20]
for value in values:
    bst.insert(value)

bst.inorder_traversal(bst.root)  # Output: 2 5 7 10 15 20



Key Operations
Search: Traverse left/right subtree based on comparison in BST.
Insertion: Add elements while maintaining the BST property.
Deletion: Requires handling three cases:
Node to delete is a leaf.
Node to delete has one child.
Node to delete has two children (replace with in-order successor or predecessor).



Trees, especially binary search trees, are fundamental in computer science 

due to their efficiency in searching, inserting, and deleting operations.





