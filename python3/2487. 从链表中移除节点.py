# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        st = list()
        cur = head
        while cur:
            v = cur.val
            while st and v > st[-1]:
                st.pop(-1)
            st.append(v)
            cur = cur.next

        ans = ListNode()
        cur = ans
        for v in st:
            cur.next = ListNode(val=v)
            cur = cur.next

        return ans.next
