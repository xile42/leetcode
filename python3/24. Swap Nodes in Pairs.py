# Given a linked list, swap every two adjacent nodes and return its head. You
# must solve the problem without modifying the values in the list's nodes (i.e.,
# only nodes themselves may be changed.)
#
#
#  Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#
#
#  Example 2:
#
#
# Input: head = []
# Output: []
#
#
#  Example 3:
#
#
# Input: head = [1]
# Output: [1]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is in the range [0, 100].
#  0 <= Node.val <= 100
#
#
#  Related Topics Linked List Recursion 👍 11932 👎 445


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def swap_two(self, pre_node):

        slow = pre_node.next
        fast = slow.next
        tmp = fast.next
        slow.next = tmp
        fast.next = slow
        pre_node.next = fast

        return slow

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pre_head = ListNode()
        pre_head.next = head

        if pre_head.next is None or pre_head.next.next is None:
            return pre_head.next

        swap_pre_head = pre_head

        while True:
            swap_pre_head = self.swap_two(swap_pre_head)
            if swap_pre_head.next is None or swap_pre_head.next.next is None:
                break

        return pre_head.next

# leetcode submit region end(Prohibit modification and deletion)