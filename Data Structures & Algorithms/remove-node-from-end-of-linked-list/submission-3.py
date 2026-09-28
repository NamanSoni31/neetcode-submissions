# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        if not head.next:
            return None
        length = 0
        val = curr
        while val: 
            length += 1
            val = val.next
        print(length)
        index = length - n + 1
        while index > 1:
            prev = curr
            curr = curr.next
            print(index)
            index -= 1
        if curr.next:
            nxt = curr.next
            if prev:
                prev.next = nxt
            else: 
                head = curr.next
                curr.next = None
        else:
            prev.next = None
        return head