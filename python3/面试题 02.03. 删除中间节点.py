# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def deleteNode(self, node):

        cur = node
        while cur.next and cur.next.next:
            cur.val = cur.next.val
            cur = cur.next

        cur.val = cur.next.val
        cur.next = None
