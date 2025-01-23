"""
Given a binary tree, return its level order traversal where the nodes in each level are ordered from left to right.

Ex: Given the following tree...

    4
   / \
  2   7
return [[4], [2, 7]]

Ex: Given the following tree...

    2
   / \
  10  15
        \
         20
return [[2], [10, 15], [20]]

Ex: Given the following tree...

    1
   / \
  9   32
 /      \
3        78
return [[1], [9, 32], [3, 78]]
"""

from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# simple approach
# def gather_levels(root):
#     if not root:
#         return []

#     cur_level_nodes = [root]
#     level_node_values = [[root.val]]

#     while cur_level_nodes:
#         next_level_nodes = []
#         next_level_node_values = []

#         for node in cur_level_nodes:
#             if node.left:
#                 next_level_nodes.append(node.left)
#                 next_level_node_values.append(node.left.val)
#             if node.right:
#                 next_level_nodes.append(node.right)
#                 next_level_node_values.append(node.right.val)

#         cur_level_nodes = next_level_nodes

#         if next_level_node_values:
#             level_node_values.append(next_level_node_values)

#     return level_node_values


def gather_levels(root):
    if not root:
        return []

    queue = deque([root])
    levels = []

    while queue:
        current_level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        levels.append(current_level)

    return levels


root = TreeNode(4, TreeNode(2), TreeNode(7))
assert gather_levels(root) == [[4], [2, 7]]

root = TreeNode(2, TreeNode(10), TreeNode(15, None, TreeNode(20)))
assert gather_levels(root) == [[2], [10, 15], [20]]

root = TreeNode(1, TreeNode(9, TreeNode(3)), TreeNode(32, None, TreeNode(78)))
assert gather_levels(root) == [[1], [9, 32], [3, 78]]
