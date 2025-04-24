# Given the head of a linked list and a value x, partition it such that all
# nodes less than x come before nodes greater than or equal to x.
#
#  You should preserve the original relative order of the nodes in each of the
# two partitions.
#
#
#  Example 1:
#
#
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
#
#
#  Example 2:
#
#
# Input: head = [2,1], x = 2
# Output: [1,2]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is in the range [0, 200].
#  -100 <= Node.val <= 100
#  -200 <= x <= 200
#
#
#  Related Topics Linked List Two Pointers 👍 7392 👎 885


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        if head is None:
            return None

        dummy_small_head = ListNode()
        dummy_big_head = ListNode()

        small, big = dummy_small_head, dummy_big_head
        node = head
        while node is not None:
            if node.val < x:
                small.next = node
                small = small.next
            else:
                big.next = node
                big = big.next
            node = node.next

        if dummy_small_head.next is None:
            return dummy_big_head.next

        small.next = dummy_big_head.next
        big.next = None

        return dummy_small_head.next

# leetcode submit region end(Prohibit modification and deletion)
