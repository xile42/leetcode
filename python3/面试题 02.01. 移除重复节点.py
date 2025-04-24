# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def removeDuplicateNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head

        vis = set()
        p = head
        cur = p.next
        vis.add(p.val)
        while cur:
            v = cur.val
            if v in vis:
                p.next = cur.next
                cur = cur.next
            else:
                p = cur
                cur = cur.next
                vis.add(v)

        return head
        
