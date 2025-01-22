"""
Given a binary search tree, return its mode (you may assume the answer is unique). 
If the tree is empty, return -1. Note: the mode is the most frequently occurring value in the tree.

Ex: Given the following tree...

        2
       / \
      1   2
return 2.


Ex: Given the following tree...

         7
        / \
      4     9
     / \   / \
    1   4 8   9
               \
                9  
return 9.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_the_mode(root):
    if not root:
        return -1

    mode = None
    max_count = 0
    current_count = 0
    prev_val = None

    def dfs(node):
        nonlocal mode, max_count, current_count, prev_val
        if not node:
            return
        dfs(node.left)
        current_count = (current_count + 1) if prev_val == node.val else 1
        if prev_val == node.val:
            current_count += 1
        else:
            current_count = 1
        if current_count > max_count:
            mode = node.val
            max_count = current_count
        prev_val = node.val
        dfs(node.right)

    dfs(root)

    return mode


root = TreeNode(2, TreeNode(1), TreeNode(2))
assert find_the_mode(root) == 2

root = TreeNode(
    7,
    TreeNode(4, TreeNode(1), TreeNode(4)),
    TreeNode(9, TreeNode(8), TreeNode(9, None, TreeNode(9))),
)
assert find_the_mode(root) == 9
