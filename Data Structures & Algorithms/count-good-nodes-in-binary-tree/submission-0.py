# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.maxVal = root.val
        def dfs(curr, maxVal):
            good = 0
            if curr:
                if curr.val >= maxVal: 
                    good += 1
                left = dfs(curr.left, max(maxVal, curr.val))
                right = dfs(curr.right, max(maxVal, curr.val))
                good += left + right
                return good
            return 0
        return dfs(root, self.maxVal)