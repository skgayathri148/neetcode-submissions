# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carryover = 0
        result = ListNode(0)
        curr = result
        while l1 or l2 or carryover:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            c = a + b + carryover
            val = c % 10
            carryover = c // 10
            result.next = ListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            result = result.next

        return curr.next