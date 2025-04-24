# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:

        vs = list()
        cur = head
        while cur:
            vs.append(cur.val)
            cur = cur.next

        return vs[::-1]
        
