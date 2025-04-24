# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head
        nodes = list()
        while cur:
            nodes.append(ListNode(cur.val))
            cur = cur.next

        if not nodes:
            return head

        head = nodes[-1]
        cur = head
        for node in nodes[::-1][1:]:
            cur.next = node
            cur = cur.next

        return head
