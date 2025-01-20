"""
Given two binary trees, return whether or not the two trees are identical. 
Note: identical meaning they exhibit the same structure and the same values at each node. 
Ex: Given the following trees...

        2
       / \
      1   3

    2
   / \
  1   3


return true.

Ex: Given the following trees...

        1
         \
          9
           \
           18

    1
   /
  9
   \
    18


return false.

Ex: Given the following trees...

        2
       / \
      3   1

    2
   / \
  1   3


return false.   
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def identical_trees(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False

    if root1.val != root2.val:
        return False

    return identical_trees(root1.left, root2.left) and identical_trees(
        root1.right, root2.right
    )


root1 = TreeNode(2, TreeNode(1), TreeNode(3))
root2 = TreeNode(2, TreeNode(1), TreeNode(3))
assert identical_trees(root1, root2) is True

root1 = TreeNode(1, None, TreeNode(9, None, TreeNode(18)))
root2 = TreeNode(1, TreeNode(9, None, TreeNode(18)))
assert identical_trees(root1, root2) is False

root1 = TreeNode(2, TreeNode(3), TreeNode(1))
root2 = TreeNode(2, TreeNode(1), TreeNode(3))
assert identical_trees(root1, root2) is False
