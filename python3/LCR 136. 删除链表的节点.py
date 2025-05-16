# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def deleteNode(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if head.val == val:
            return head.next

        cur = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                break
            cur = cur.next

        return head
