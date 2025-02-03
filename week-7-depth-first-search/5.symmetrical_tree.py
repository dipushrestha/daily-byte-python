"""
Given a binary tree, return whether or not it forms a reflection across its center 
(i.e. a line drawn straight down starting from the root).
Note: a reflection is when an image, flipped across a specified line, forms the same image.

Ex: Given the following tree…

   2
 /   \
1     1
return true as when the tree is reflected across its center all the nodes match.

Ex: Given the following tree…

    1
   / \
  5   5
   \    \
    7    7
return false as when the tree is reflected across its center the nodes containing sevens do not match.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def symmetrical_tree(root):
    if not root:
        return True

    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return True

        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    return is_mirror(root.left, root.right)


root = TreeNode(2, TreeNode(1), TreeNode(1))
assert symmetrical_tree(root) is True

root = TreeNode(1, TreeNode(5, None, TreeNode(7)), TreeNode(5, None, TreeNode(7)))
assert symmetrical_tree(root) is False


root = TreeNode(
    1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))
)
assert symmetrical_tree(root) is True

root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
assert symmetrical_tree(root) is False
