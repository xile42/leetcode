# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def swapNodes(self, head: ListNode, k: int) -> ListNode:

        p, q, n = head, head, head
        i = 1
        while n:
            if i < k:
                p = p.next  # 正数第k个
            if i > k:
                q = q.next  # 倒数第k个
            n = n.next
            i += 1
        p.val, q.val = q.val, p.val

        return head
