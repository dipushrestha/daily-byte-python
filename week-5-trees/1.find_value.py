'''
This question is asked by Google. Given the reference to the root of a binary 
search tree and a search value, return the reference to the node that contains 
the value if it exists and null otherwise.
Note: all values in the binary search tree will be unique.

Ex: Given the tree...

        3
       / \
      1   4
and the search value 1 return a reference to the node containing 1.

Ex: Given the following tree...

        7
       / \
      5   9
         / \ 
        8   10
and the search value 9 return a reference to the node containing 9.

Ex: Given the following tree...

        8
       / \
      6   9
and the search value 7 return null.
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_value(root_node, search_val):
    cur_node = root_node

    while cur_node:
        if cur_node.val == search_val:
            return cur_node
        elif cur_node.val > search_val:
            cur_node = cur_node.left
        else:
            cur_node = cur_node.right

    return None 

root_node = TreeNode(3)
root_node.left = TreeNode(1)
root_node.right = TreeNode(4)
assert find_value(root_node, 1).val == 1

root_node = TreeNode(7)
root_node.left = TreeNode(5)
root_node.right = TreeNode(9)
root_node.right.left = TreeNode(8)
root_node.right.right = TreeNode(10)
assert find_value(root_node, 9).val == 9

root_node = TreeNode(8)
root_node.left = TreeNode(6)
root_node.right = TreeNode(9)
assert find_value(root_node, 7) == None
