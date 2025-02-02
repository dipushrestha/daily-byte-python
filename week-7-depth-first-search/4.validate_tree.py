"""
Given a binary tree, containing unique values, determine if it is a valid binary search tree.
Note: the invariants of a binary search tree (in our case) are all values to the left of a given 
node are less than the current node’s value, all values to the right of a given node are greater 
than the current node’s value, and both the left and right subtrees of a given node must also be binary search trees.

Ex: Given the following binary tree…

   1
 /   \
2     3
return false.

Ex: Given the following tree…

   2
 /   \
1     3
return true.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def validate_tree(root, min_val=float("-inf"), max_val=float("inf")):
    if not root:
        return True

    if not (min_val < root.val < max_val):
        return False

    return validate_tree(root.left, min_val, root.val) and validate_tree(
        root.right, root.val, max_val
    )


root = TreeNode(1, TreeNode(2), TreeNode(3))
assert validate_tree(root) is False

root = TreeNode(2, TreeNode(1), TreeNode(3))
assert validate_tree(root) is True

root = TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(4)))
assert validate_tree(root) is False
