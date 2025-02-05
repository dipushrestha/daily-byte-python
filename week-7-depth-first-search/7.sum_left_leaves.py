"""
Given a binary tree, return the sum of all left leaves of the tree. Ex: Given the following tree…

    5
   / \
  2   12
     /  \
    3    8
return 5 (i.e. 2 + 3)

Ex: Given the following tree…

       2
      / \
    4    2
   / \ 
  3   9 
return 3
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_left_leaves(root):
    if not root:
        return 0

    left_leaf_val = 0

    if root.left and not root.left.left and not root.left.right:
        left_leaf_val = root.left.val

    return left_leaf_val + sum_left_leaves(root.left) + sum_left_leaves(root.right)


root = TreeNode(5, TreeNode(2), TreeNode(12, TreeNode(3), TreeNode(8)))
assert sum_left_leaves(root) == 5

root = TreeNode(2, TreeNode(4, TreeNode(3), TreeNode(9)), TreeNode(2))
assert sum_left_leaves(root) == 3
