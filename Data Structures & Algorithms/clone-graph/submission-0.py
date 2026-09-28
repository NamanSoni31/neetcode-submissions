"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        final = {}
        if not node: 
            return None
        def bfs(node):
            if node not in final:
                newNode = Node(node.val, None)
                final[node] = newNode
                if node.neighbors:
                    for neighbor in node.neighbors: 
                        nei = bfs(neighbor)
                        newNode.neighbors.append(nei)
                return newNode
            if node in final:
                return final[node]
        bfs(node)
        return final[node]