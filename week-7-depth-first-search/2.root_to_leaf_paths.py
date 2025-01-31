"""
Given a binary tree, return a list of strings containing all root to leaf paths.

Ex: Given the following tree…

   1
 /   \
2     3
return ["1->2", "1->3"]

Ex: Given the following tree…

    8
   / \
  2  29
    /  \
   3    9
return ["8->2", "8->29->3", "8->29->9"]
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def root_to_leaf_paths(root):
    paths = []

    def dfs(node, current_path):
        if not node:
            return

        current_path.append(str(node.val))

        if not node.left and not node.right:
            paths.append("->".join(current_path))

        dfs(node.left, current_path)
        dfs(node.right, current_path)
        current_path.pop()

    dfs(root, [])
    return paths


root = TreeNode(1, TreeNode(2), TreeNode(3))
assert root_to_leaf_paths(root) == ["1->2", "1->3"]

root = TreeNode(8, TreeNode(2), TreeNode(29, TreeNode(3), TreeNode(9)))
assert root_to_leaf_paths(root) == ["8->2", "8->29->3", "8->29->9"]
