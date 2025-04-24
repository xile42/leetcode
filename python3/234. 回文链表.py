# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        vs = list()
        
        while head is not None:
            vs.append(head.val)
            head = head.next

        return vs == vs[::-1]
