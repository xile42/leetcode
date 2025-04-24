# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def trainningPlan(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        cur = head
        while l1 or l2:
            if l1 is None or (l2 and l2.val <= l1.val):
                cur.next = l2
                l2 = l2.next
                cur = cur.next
                cur.next = None
            else:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
                cur.next = None

        return head.next
        
