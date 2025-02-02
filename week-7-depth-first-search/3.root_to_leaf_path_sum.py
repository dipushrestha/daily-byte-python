"""
Given a binary tree and a target, return whether or not there exists a root to leaf path such that all values along the path sum to the target.

Ex: Given the following tree…

      1
     / \
    5   2
   /   / \
  1  12   29
and a target of 15, return true as the path 1->2->12 sums to 15.

Ex: Given the following tree…

     104
    /   \
  39     31
 / \    /  \
32  1  9    10
and a target of 175, return true as the path 104->39->32 sums to 175.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def root_to_leaf_path_sum(root, sum):
    if not root:
        return False

    if not root.left and not root.right:
        return sum == root.val

    return root_to_leaf_path_sum(root.left, sum - root.val) or root_to_leaf_path_sum(
        root.right, sum - root.val
    )


root = TreeNode(1, TreeNode(5, TreeNode(1)), TreeNode(2, TreeNode(12), TreeNode(29)))
assert root_to_leaf_path_sum(root, 15) is True

root = TreeNode(
    104,
    TreeNode(39, TreeNode(32), TreeNode(1)),
    TreeNode(31, TreeNode(9), TreeNode(10)),
)
assert root_to_leaf_path_sum(root, 175) is True
