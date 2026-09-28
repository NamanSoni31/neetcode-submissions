# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:     
        values = self.levelOrder(root)
        final = []
        for i in values:
            final.append(i[-1])
        return final
    
    def levelOrder(self, root):
        queue = deque()
        lst = []
        if not root:
            return lst
        queue.append(root)
        while queue:
            level_size = len(queue)
            current_level = []
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                current_level.append(node.val)
            lst.append(current_level)
        return lst