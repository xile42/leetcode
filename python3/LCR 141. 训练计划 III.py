# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def trainningPlan(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node = ListNode()
        cur = node
        for v in self.f(head):
            cur.next = ListNode(val=v)
            cur = cur.next

        return node.next

    def f(self, head):

        if head is None:
            return list()

        return self.f(head.next) + [head.val]
