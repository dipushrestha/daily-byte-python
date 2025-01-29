"""
Given a binary tree, return its column order traversal from top to bottom and 
left to right. Note: if two nodes are in the same row and column, order them from left to right.

Ex: Given the following tree…

    8
   / \
  2   29
     /  \
    3    9
return [[2], [8, 3], [29], [9]]

Ex: Given the following tree…

     100
    /   \
  53     78
 / \    /  \
32  3  9    20
return [[32], [53], [100, 3, 9], [78], [20]]
"""

from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def gather_columns(root):
    if not root:
        return []

    queue = deque()
    queue.append((root, 0, 0))  # (node, column, level)
    nodes = []
    index = 0  # To track the order of processing

    while queue:
        node, col, lvl = queue.popleft()
        nodes.append((col, lvl, index, node.val))
        index += 1

        if node.left:
            queue.append((node.left, col - 1, lvl + 1))
        if node.right:
            queue.append((node.right, col + 1, lvl + 1))

    nodes.sort(key=lambda x: (x[0], x[1], x[2]))

    result = []
    prev_col = None
    for node in nodes:
        current_col = node[0]
        value = node[3]
        if current_col != prev_col:
            result.append([value])
            prev_col = current_col
        else:
            result[-1].append(value)

    return result


root = TreeNode(8, TreeNode(2), TreeNode(29, TreeNode(3), TreeNode(9)))
assert gather_columns(root) == [[2], [8, 3], [29], [9]]

root = TreeNode(
    100,
    TreeNode(53, TreeNode(32), TreeNode(3)),
    TreeNode(78, TreeNode(9), TreeNode(20)),
)
assert gather_columns(root) == [[32], [53], [100, 3, 9], [78], [20]]
