# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head:
            return None

        ns = list()
        cur = head
        while cur:
            ns.append(cur.val)
            cur = cur.next

        node = ListNode()
        cur = node
        for v in ns:
            if v != val:
                cur.next = ListNode(v)
                cur = cur.next

        return node.next
