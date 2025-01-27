"""
Given a binary tree, return its zig-zag level order traversal (i.e. its level order 
traversal from left to right the first level, right to left the level the second, etc.).

Ex: Given the following tree…

    1
   / \
  2   3
return [[1], [3, 2]]

Ex: Given the following tree…

    8
   / \
  2  29
    /  \
   3    9
return [[8], [29, 2], [3, 9]]
"""

from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_traversal(root):
    if not root:
        return []

    queue = deque([root])
    levels = []
    reverse = False

    while queue:
        current_level = deque()
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            if reverse:
                current_level.appendleft(node.val)
            else:
                current_level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        levels.append(list(current_level))
        reverse = not reverse

    return levels


root = TreeNode(1, TreeNode(2), TreeNode(3))
assert zigzag_traversal(root) == [[1], [3, 2]]

root = TreeNode(8, TreeNode(2), TreeNode(29, TreeNode(3), TreeNode(9)))
assert zigzag_traversal(root) == [[8], [29, 2], [3, 9]]
