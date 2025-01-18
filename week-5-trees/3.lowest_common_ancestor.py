'''
Given a binary search tree that contains unique values and two nodes within
the tree, a, and b, return their lowest common ancestor.
Note: the lowest common ancestor of two nodes is the deepest node within the 
tree such that both nodes are descendants of it.

Ex: Given the following tree...
       7
      / \
    2    9
   / \ 
  1   5 
and a = 1, b = 9, return a reference to the node containing 7.

Ex: Given the following tree...

        8
       / \
      3   9
     / \ 
    2   6
and a = 2, b = 6, return a reference to the node containing 3.

Ex: Given the following tree...

        8
       / \
      6   9
and a = 6, b = 8, return a reference to the node containing 8.
'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
# naive brute force approach
def lowest_common_ancestor(root, a, b):
    cur = root
    a_parents = []
    b_parents = []

    while cur:
        if cur.val == a:
            if len(a_parents) == 0: 
                a_parents.append(root)
            break
        elif cur.val > a:
            a_parents.append(cur)
            cur = cur.left
        else:
            a_parents.append(cur)
            cur = cur.right
    
    cur = root
                
    while cur:
        if cur.val == b:
            if len(b_parents) == 0: 
                b_parents.append(root)
            break
        elif cur.val > b:
            b_parents.append(cur)
            cur = cur.left
        else:
            b_parents.append(cur)
            cur = cur.right

    for i in range(len(a_parents)-1, -1, -1):
        for j in range(len(b_parents)-1, -1, -1):
            if a_parents[i] and b_parents[j] and a_parents[i].val == b_parents[j].val:
                return a_parents[i]
    
    return None
'''

'''
# generic binary tree solution
def lowest_common_ancestor(root, a, b):
    cur = root

    if not cur or cur.val == a or cur.val == b:
        return cur
    
    left = lowest_common_ancestor(cur.left, a, b)
    right = lowest_common_ancestor(cur.right, a, b)

    if left and right:
        return cur
    else:
        return left or right
'''

def lowest_common_ancestor(root, a, b):
    cur = root

    while cur:
        if a < cur.val and b < cur.val:
            cur = cur.left
        elif a > cur.val and b > cur.val:
            cur = cur.right
        else:
            return cur
        
    return None


root = TreeNode(7, TreeNode(2, TreeNode(1), TreeNode(5)), TreeNode(9))
assert lowest_common_ancestor(root, 1, 9).val == 7

root = TreeNode(8, TreeNode(3, TreeNode(2), TreeNode(6)), TreeNode(9))
assert lowest_common_ancestor(root, 2, 6).val == 3

root = TreeNode(8, TreeNode(6), TreeNode(9))
assert lowest_common_ancestor(root, 6, 8).val == 8
