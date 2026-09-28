# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(p, q):
            if not p and not q:
                if self.res:
                    self.res = True
            else:
                if not p and q: 
                    self.res = False
                    return 0 
                elif p and not q:
                    self.res = False
                    return 0 
                if p and q: 
                    if self.res:
                        if p.val == q.val:
                            self.res = True
                            dfs(p.left, q.left)
                            dfs(p.right, q.right)
                        else:
                            self.res = False
                    return 0 
        dfs(p, q)
        return self.res
                
            