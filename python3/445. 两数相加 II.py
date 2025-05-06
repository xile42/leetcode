# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def f(node):

            if node is None:
                return str()

            return str(node.val) + f(node.next)

        v = str(int(f(l1)) + int(f(l2)))

        ans = ListNode()
        cur = ans
        for c in v:
            cur.next = ListNode(val=int(c))
            cur = cur.next

        return ans.next
