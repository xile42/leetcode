# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:

        dummy = ListNode(next=head)
        cur = dummy
        fast = dummy
        while True:
            i = 0
            while cur.next and i < m:
                cur = cur.next
                fast = fast.next
                i += 1
            if not fast.next:
                break
            i = 0
            while fast.next and i < n:
                fast = fast.next
                i += 1
            cur.next = fast.next

        return dummy.next
