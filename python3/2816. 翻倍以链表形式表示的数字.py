# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def f(node):

            if node is None:
                return 0

            v = f(node.next)
            c = (node.val * 2 + v) // 10
            node.val = (node.val * 2 + v) % 10

            return c

        v = f(head)
        if v:
            dummy = ListNode(v)
            dummy.next = head
            head = dummy

        return head
