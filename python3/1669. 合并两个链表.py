# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        h2 = list2
        cur = list2
        while cur.next:
            cur = cur.next
        t2 = cur

        dummy = ListNode(next=list1)
        pre = dummy
        cur = list1
        cnt = 0
        while cnt != a:
            cur = cur.next
            pre = pre.next
            cnt += 1
        while cnt != b:
            cur = cur.next
            cnt += 1
        tail = cur.next

        pre.next = h2
        t2.next = tail

        return dummy.next
