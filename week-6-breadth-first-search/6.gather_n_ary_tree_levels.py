"""
Given an n-ary tree, return its level order traversal.
Note: an n-ary tree is a tree in which each node has no more than N children.

Ex: Give the following n-ary tree…

    8
  / | \
 2  3  29
return [[8], [2, 3, 29]]

Ex: Given the following n-ary tree…

     2
   / | \
  1  6  9
 /   |   \
8    2    2
   / | \
 19 12 90
return [[2], [1, 6, 9], [8, 2, 2], [19, 12, 90]]
"""

from collections import deque


class NAryTreeNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children if children else []


def gather_n_ary_tree_levels(root):
    if not root:
        return []

    queue = deque([root])
    levels = []

    while queue:
        current_level = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            for child in node.children:
                queue.append(child)

        levels.append(current_level)

    return levels


root = NAryTreeNode(8, [NAryTreeNode(2), NAryTreeNode(3), NAryTreeNode(29)])
assert gather_n_ary_tree_levels(root) == [[8], [2, 3, 29]]

root = NAryTreeNode(
    2,
    [
        NAryTreeNode(1, [NAryTreeNode(8)]),
        NAryTreeNode(
            6,
            [
                NAryTreeNode(2, [NAryTreeNode(19), NAryTreeNode(12), NAryTreeNode(90)]),
            ],
        ),
        NAryTreeNode(9, [NAryTreeNode(2)]),
    ],
)
assert gather_n_ary_tree_levels(root) == [[2], [1, 6, 9], [8, 2, 2], [19, 12, 90]]
