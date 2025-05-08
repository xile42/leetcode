# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = fast = head
        cnt = 1
        while fast.next:
            fast = fast.next
            cnt += 1
            if cnt & 1:
                slow = slow.next

        if not cnt & 1 and slow.next:
            slow = slow.next

        return slow
