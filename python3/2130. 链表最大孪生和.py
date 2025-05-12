# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def pairSum(self, head: Optional[ListNode]) -> int:

        ns = list()
        cur = head
        while cur:
            ns.append(cur.val)
            cur = cur.next

        ans = -inf
        for i in range(len(ns) // 2):
            ans = max(ans, ns[i] + ns[len(ns) - 1 - i])

        return ans
