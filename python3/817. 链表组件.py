# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:

        s = set(nums)
        ns = list()
        cur = head
        while cur:
            ns.append(1 if cur.val in s else -1)
            cur = cur.next

        ans = 0
        for c, ite in groupby(ns):
            if c != -1:
                ans += 1

        return ans
