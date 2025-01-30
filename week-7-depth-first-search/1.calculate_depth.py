"""
Given a binary tree, return its maximum depth.
Note: the maximum depth is defined as the number of nodes along the longest path from root node to leaf node.

Ex: Given the following tree…

    9
   / \
  1   2
return 2

Ex: Given the following tree…

    5
   / \
  1  29
    /  \
   4   13
return 3
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def calculate_depth(root):
    if not root:
        return 0

    return 1 + max(calculate_depth(root.left), calculate_depth(root.right))


root = TreeNode(9, TreeNode(1), TreeNode(2))
assert calculate_depth(root) == 2

root = TreeNode(5, TreeNode(1), TreeNode(29, TreeNode(4), TreeNode(13)))
assert calculate_depth(root) == 3
