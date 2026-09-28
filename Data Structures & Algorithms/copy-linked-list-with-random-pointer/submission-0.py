"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        copy = Node(0, None, None)
        d = {}
        d[None] = None
        while node:
            copy = Node(node.val)
            d[node] = copy
            node = node.next
        second = head
        while second:
            third = second.next
            fourth = second.random
            if third in d: 
                d[second].next = d[third]
            if fourth in d:
                d[second].random = d[fourth]
            second = second.next
        return d[head]