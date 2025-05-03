# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head
        s = set()
        while cur:
            if cur in s:
                return cur
            s.add(cur)
            cur = cur.next

        return None
