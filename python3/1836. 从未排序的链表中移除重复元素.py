# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def deleteDuplicatesUnsorted(self, head: Optional[ListNode]) -> Optional[ListNode]:

        c = Counter()
        cur = head
        while cur:
            c[cur.val] += 1
            cur = cur.next

        dummy = ListNode(next=head)
        cur = dummy
        fast = cur.next
        while fast:
            if c[fast.val] > 1:
                fast = fast.next
            else:
                cur.next = fast
                cur = cur.next
                fast = fast.next

        cur.next = None

        return dummy.next
