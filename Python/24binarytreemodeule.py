#Write a program in Python to Create binarytree from the given list using Binary tree module in python.
from binarytree import build

# Function to create binary tree from a given list
def create_binary_tree_from_list(values):
    """
    Create a binary tree from a list of values.

    Args:
        values (list): A list of integers or None values.

    Returns:
        Node: Root node of the binary tree.
    """
    # Build the binary tree using the binarytree module
    tree = build(values)
    return tree

# Example list to create binary tree
values = [1, 2, 3, 4, 5, 6, 7]

# Create the binary tree
binary_tree = create_binary_tree_from_list(values)

# Print the binary tree
print("Binary Tree:")
print(binary_tree)