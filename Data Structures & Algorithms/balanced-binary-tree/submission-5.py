# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        if not root: 
            return True

        def dfs(curr):
            if not curr: 
                return 0
            else: 
                left = dfs(curr.left)
                right = dfs(curr.right)
                if abs(left - right) > 1:
                    self.res = False
                else: 
                    if not self.res:
                        self.res = False
                    else:
                        self.res = True
                return 1 + max(left, right)
        
        dfs(root)
        return self.res