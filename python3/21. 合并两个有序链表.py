# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        cur = head
        while list1 or list2:
            if list1 is None or (list2 and list1.val > list2.val):
                cur.next = list2
                cur = cur.next
                list2 = list2.next
                cur.next = None
            else:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
                cur.next = None

        return head.next
