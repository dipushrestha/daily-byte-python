"""
Given a binary tree, return the largest value in each of its levels. Ex: Given the following tree…

    2
   / \
  10  15
        \
         20
return [2, 15, 20]

Ex: Given the following tree…

          1
         / \
        5   6
       / \   \  
      5   3   7 
return [1, 6, 7]
"""

from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_value_in_each_level(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        level_max = float("-inf")
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level_max = max(node.val, level_max)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_max)

    return result


root = TreeNode(2, TreeNode(10), TreeNode(15, None, TreeNode(20)))
assert max_value_in_each_level(root) == [2, 15, 20]

root = TreeNode(
    1, TreeNode(5, TreeNode(5), TreeNode(3)), TreeNode(6, None, TreeNode(7))
)
assert max_value_in_each_level(root) == [1, 6, 7]
