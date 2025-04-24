# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        na = list()
        nb = list()
        
        cur = headA
        while cur:
            na.append(cur)
            cur = cur.next

        cur = headB
        while cur:
            nb.append(cur)
            cur = cur.next

        na = na[::-1]
        nb = nb[::-1]

        ans = None
        for a, b in zip(na, nb):
            if a is b:
                ans = a
            else:
                break

        return ans
