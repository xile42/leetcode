# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:

        cur = head
        while cur:
            if cur.val == inf:
                return True
            cur.val = inf
            cur = cur.next

        return False
