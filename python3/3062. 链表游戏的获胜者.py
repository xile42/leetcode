# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def gameResult(self, head: Optional[ListNode]) -> str:

        ns = list()
        cur = head
        while cur:
            ns.append(cur.val)
            cur = cur.next

        ans = sum([1 if ns[i] < ns[i + 1] else -1 for i in range(0, len(ns), 2)])

        return "Odd" if ans > 0 else ("Even" if ans < 0 else "Tie")
