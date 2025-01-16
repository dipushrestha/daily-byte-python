'''
Given a binary search tree, rearrange the tree such that it forms a linked list where all its values are in ascending order.

Ex: Given the following tree...
        5
       / \
      1   6

return...

1
 \
  5
   \
    6

Ex: Given the following tree...

       5
      / \
    2    9
   / \ 
  1   3 

return...

1
 \
  2
   \
    3
     \
      5
       \
        9

Ex: Given the following tree...

5
 \
  6

return...

5
 \
  6
'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convert_binary_tree_to_sorted_linked_list(root):
    dummy = TreeNode(root.val)
    cur = dummy

    def inorder_traversal(node):
        nonlocal cur
        if not node:
            return
        inorder_traversal(node.left)
        cur.right = node
        cur.left = None
        cur = cur.right
        inorder_traversal(node.right)

    inorder_traversal(root)
    return dummy.right

def tree_list_str(root):
    cur = root
    result = []
    while cur:
        result.append(str(cur.val))
        cur = cur.right
    return "->".join(result)

root = TreeNode(5, TreeNode(1), TreeNode(6))
assert tree_list_str(convert_binary_tree_to_sorted_linked_list(root)) == "1->5->6"

root = TreeNode(5, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(9))
assert tree_list_str(convert_binary_tree_to_sorted_linked_list(root)) == "1->2->3->5->9"

root = TreeNode(5, None, TreeNode(6))
assert tree_list_str(convert_binary_tree_to_sorted_linked_list(root)) == "5->6"
