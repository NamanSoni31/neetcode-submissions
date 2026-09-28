# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lower, upper):  
            if not root: 
                return True
            elif root.val > lower and root.val < upper: 
                return dfs(root.right, root.val, upper) and dfs(root.left, lower, root.val)
            else:
                return False

        return dfs(root, -math.inf, math.inf)