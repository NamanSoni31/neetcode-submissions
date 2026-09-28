# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        n = 0
        l3 = ListNode(0)
        start = l3
        while l1 or l2:
            if l1 == None and l2 == None:
                return total
            elif l1 == None:
                total += l2.val * (10 ** n)
                l2 = l2.next
            elif l2 == None: 
                total += l1.val * (10 ** n)
                l1 = l1.next
            else:
                value = l1.val + l2.val
                total += value * (10**n)
                l1 = l1.next
                l2 = l2.next
            n += 1
        print(n)
        print(total)
        if total == 0:
            l3 = ListNode(0)
            return l3
        while total > 0:
            value = total % 10
            total = total // 10
            l3.next = ListNode(value)
            l3 = l3.next
        return start.next