# Given the head of a sorted linked list, delete all nodes that have duplicate
# numbers, leaving only distinct numbers from the original list. Return the linked
# list sorted as well.
#
#
#  Example 1:
#
#
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
#
#
#  Example 2:
#
#
# Input: head = [1,1,1,2,3]
# Output: [2,3]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is in the range [0, 300].
#  -100 <= Node.val <= 100
#  The list is guaranteed to be sorted in ascending order.
#
#
#  Related Topics Linked List Two Pointers 👍 8882 👎 246


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head

        dummy_head = ListNode(val=float("inf"))
        dummy_head.next = None
        slow = dummy_head
        fast = head
        pre_fast = dummy_head

        while True:

            while fast.next is not None and fast.val == fast.next.val:
                pre_fast = fast
                fast = fast.next

            if pre_fast.val != fast.val:
                slow.next = ListNode(val=fast.val)
                slow = slow.next

            if fast.next is None:
                break

            pre_fast = fast
            fast = fast.next

        return dummy_head.next

# leetcode submit region end(Prohibit modification and deletion)
