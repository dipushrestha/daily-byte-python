'''
Given an array of numbers sorted in ascending order, return a height-balanced 
binary search tree using every number from the array.
Note: height-balanced meaning that the level of any node’s two subtrees should not differ by more than one.

Ex: Given the following nums...

nums = [1, 2, 3] return a reference to the following tree...
       2
      /  \
     1    3

Ex: Given the following nums...

nums = [1, 2, 3, 4, 5, 6] return a reference to the following tree...
        3
       / \
      2   5
     /   / \
    1   4   6
'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not other:
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right

def sorted_array_to_binary_search_tree(nums):
    def build_tree(low, high):
        if low > high:
            return None

        mid = (low + high) // 2
        root = TreeNode(nums[mid])
        root.left = build_tree(low, mid - 1)
        root.right = build_tree(mid + 1, high)

        return root

    return build_tree(0, len(nums) - 1)

nums = [1, 2, 3]
assert sorted_array_to_binary_search_tree(nums) == TreeNode(2, TreeNode(1), TreeNode(3))

nums = [1, 2, 3, 4, 5, 6]
assert sorted_array_to_binary_search_tree(nums) == TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(5, TreeNode(4), TreeNode(6)))
