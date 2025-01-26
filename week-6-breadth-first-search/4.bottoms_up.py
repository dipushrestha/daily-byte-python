"""
Given a binary tree, returns of all its levels in a bottom-up fashion 
(i.e. last level towards the root). Ex: Given the following tree…

        2
       / \
      1   2
return [[1, 2], [2]]

Ex: Given the following tree…

       7
      / \
    6    2
   / \ 
  3   3 
return [[3, 3], [6, 2], [7]]
"""

from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bottoms_up(root):
    if not root:
        return []

    levels = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        levels.append(current_level)

    return levels[::-1]


root = TreeNode(2, TreeNode(1), TreeNode(2))
assert bottoms_up(root) == [[1, 2], [2]]

root = TreeNode(7, TreeNode(6, TreeNode(3), TreeNode(3)), TreeNode(2))
assert bottoms_up(root) == [[3, 3], [6, 2], [7]]
