# Given the head of a linked list, rotate the list to the right by k places.
#
#
#  Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
#
#
#  Example 2:
#
#
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is in the range [0, 500].
#  -100 <= Node.val <= 100
#  0 <= k <= 2 * 10⁹
#
#
#  Related Topics Linked List Two Pointers 👍 9788 👎 1458


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None:
            return None

        length = 0
        node = head
        while node is not None:
            node = node.next
            length += 1

        k = k % length

        if k == 0:
            return head

        fast = head
        slow = head
        for _ in range(k):
            fast = fast.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head

# leetcode submit region end(Prohibit modification and deletion)
