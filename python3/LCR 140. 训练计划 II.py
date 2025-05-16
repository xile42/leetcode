# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:

        k = 1
        fast = head
        slow = head
        while k != cnt:
            fast = fast.next
            k += 1
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        return slow
