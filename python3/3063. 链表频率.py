# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ns = list()
        cur = head
        while cur:
            ns.append(cur.val)
            cur = cur.next

        head = ListNode()
        cur = head
        for v in Counter(ns).values():
            node = ListNode(v)
            cur.next = node
            cur = cur.next

        return head.next
