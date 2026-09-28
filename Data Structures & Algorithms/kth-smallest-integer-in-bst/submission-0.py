# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.num = k
        def inOrder(root):
            if root:
                left = inOrder(root.left)
                if left is not None: 
                    return left
                print(root.val)
                self.num -= 1
                if self.num == 0: 
                    return root.val
                right = inOrder(root.right)
                if right is not None:
                    return right

        return inOrder(root)