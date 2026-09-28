# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = head
        if not head:
            return None
        if not head.next:
            l4 = head
        l2 = head.next
        while l2 and l2.next: 
            l1 = l1.next
            l2 = l2.next.next
        second = l1.next
        l1.next = None
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        first = head
        second = prev
        while second:
            firstnxt = first.next
            secondnxt = second.next
            first.next = second
            second.next = firstnxt
            first = firstnxt
            second = secondnxt