"""
Given two binary trees, return whether or not both trees have the same leaf sequence. 
Two trees have the same leaf sequence if both trees’ leaves read the same from left to right.

Ex: Given the following trees…

   1
 /   \
1     3

and


   7
 /   \
1     2

return false as both the trees' leaves don't read the same from left to right (i.e. [1, 3] and [1, 2]).

Ex: Given the following trees…

    8
   / \
  2   29
    /  \
   3    9

and

    8
   / \
  2  29
 /   /  \
2   3    9
     \
      3
return true as both the trees' leaves read the same from left to right (i.e. [2, 3, 9] and [2, 3, 9]).
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def same_leaves(root1, root2):
    def dfs(node, leaves):
        if not node:
            return

        if not node.left and not node.right:
            leaves.append(node.val)

        dfs(node.left, leaves)
        dfs(node.right, leaves)

    leaves1, leaves2 = [], []
    dfs(root1, leaves1)
    dfs(root2, leaves2)

    return leaves1 == leaves2


root1 = TreeNode(1, TreeNode(1), TreeNode(3))
root2 = TreeNode(7, TreeNode(1), TreeNode(2))
assert same_leaves(root1, root2) is False

root1 = TreeNode(8, TreeNode(2), TreeNode(29, TreeNode(3), TreeNode(9)))
root2 = TreeNode(
    8,
    TreeNode(2, TreeNode(2)),
    TreeNode(29, TreeNode(3, None, TreeNode(3)), TreeNode(9)),
)
assert same_leaves(root1, root2) is True
