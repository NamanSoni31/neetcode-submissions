# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        dummy = ListNode()
        if not curr1: 
            return list2
        elif not curr2: 
            return list1
        if curr1 and curr1.val <= curr2.val:
            dummy = curr1
            curr1 = curr1.next
        elif curr2 and curr2.val < curr1.val:
            dummy = curr2
            curr2 = curr2.next
        well = dummy
        while curr1 and curr2: 
            if curr1.val < curr2.val:
                dummy.next = curr1
                curr1 = curr1.next
                dummy = dummy.next
            else: 
                dummy.next = curr2
                curr2 = curr2.next
                dummy = dummy.next
        while curr1: 
            dummy.next = curr1
            dummy = dummy.next
            curr1 = curr1.next
        while curr2: 
            dummy.next = curr2
            curr2 = curr2.next
            dummy = dummy.next
        return well