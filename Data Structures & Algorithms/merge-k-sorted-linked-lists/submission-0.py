# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            dummy = ListNode(0)
            return dummy.next

        if len(lists) == 1:
            return lists[0]

        for i in range(1, len(lists)):
            l1, l2 = lists[i-1], lists[i]
            result = ListNode(0)
            dummy = result
            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2= l2.next
                dummy = dummy.next
            if l1 or l2:
                dummy.next = l1 if l1 else l2
                dummy = dummy.next

            lists[i] = result.next

        return lists[-1]
