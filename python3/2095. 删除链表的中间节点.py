# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head.next
        slow = head
        dummy = ListNode(next=head)
        pre_slow = dummy
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
            pre_slow = pre_slow.next

        pre_slow.next = slow.next

        return dummy.next
