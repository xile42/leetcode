# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        vs = list()
        cur = head
        while cur is not None:
            vs.append(cur.val)
            cur = cur.next

        return vs == vs[::-1]
