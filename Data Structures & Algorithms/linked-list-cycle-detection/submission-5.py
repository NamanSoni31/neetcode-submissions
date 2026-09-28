# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: 
            return False
        i = head
        j = head
        if i.next == None:
            return False
        while j.next and i.next:
            i = i.next
            j = j.next.next
            if j == None:
                return False
            if j == i:
                return True
        return False