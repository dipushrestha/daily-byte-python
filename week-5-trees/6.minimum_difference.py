"""
Given a binary search tree, return the minimum difference between any two nodes in the tree.

Ex: Given the following tree...
        2
       / \
      3   1
return 1.

Ex: Given the following tree...
        29
       /  \
     17   50
    /     / \
   1    42  59
return 8.

Ex: Given the following tree...
        2
         \
         100
return 98.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minimum_difference(root):
    prev, res = None, float("inf")

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        nonlocal prev, res
        if prev:
            res = min(res, abs(node.val - prev.val))
        prev = node
        dfs(node.right)

    dfs(root)
    return res


root = TreeNode(2, TreeNode(3), TreeNode(1))
assert minimum_difference(root) == 1

root = TreeNode(29, TreeNode(17, TreeNode(1)), TreeNode(50, TreeNode(42), TreeNode(59)))
assert minimum_difference(root) == 8

root = TreeNode(2, None, TreeNode(100))
assert minimum_difference(root) == 98
