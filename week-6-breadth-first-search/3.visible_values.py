"""
Given a binary tree return all the values you’d be able to see if you were 
standing on the left side of it with values ordered from top to bottom.

Ex: Given the following tree…

-->    4
      / \
-->  2   7
return [4, 2]

Ex: Given the following tree…

-->        7
         /  \
-->     4     9
       / \   / \
-->   1   4 8   9
                 \
-->               9
return [7, 4, 1, 9]
"""

from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def visible_values(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        result.append(queue[0].val)
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


root = TreeNode(4, TreeNode(2), TreeNode(7))
assert visible_values(root) == [4, 2]

root = TreeNode(
    7,
    TreeNode(4, TreeNode(1), TreeNode(4)),
    TreeNode(9, TreeNode(8), TreeNode(9, None, TreeNode(9))),
)
assert visible_values(root) == [7, 4, 1, 9]
