# Given the head of a singly linked list and two integers left and right where
# left <= right, reverse the nodes of the list from position left to position
# right, and return the reversed list.
#
#
#  Example 1:
#
#
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
#
#
#  Example 2:
#
#
# Input: head = [5], left = 1, right = 1
# Output: [5]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is n.
#  1 <= n <= 500
#  -500 <= Node.val <= 500
#  1 <= left <= right <= n
#
#
#
# Follow up: Could you do it in one pass?
#
#  Related Topics Linked List 👍 11712 👎 629


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        nums = list()
        node = head
        while node is not None:
            nums.append(node.val)
            node = node.next

        left -= 1
        right -= 1
        nums[left:right+1] = nums[left:right+1][::-1]

        new_head = ListNode()
        node = new_head
        for num in nums:
            this_node = ListNode(num)
            node.next = this_node
            node = node.next

        return new_head.next

# leetcode submit region end(Prohibit modification and deletion)
