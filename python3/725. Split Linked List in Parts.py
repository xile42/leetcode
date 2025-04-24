# Given the head of a singly linked list and an integer k, split the linked
# list into k consecutive linked list parts.
#
#  The length of each part should be as equal as possible: no two parts should
# have a size differing by more than one. This may lead to some parts being null.
#
#  The parts should be in the order of occurrence in the input list, and parts
# occurring earlier should always have a size greater than or equal to parts
# occurring later.
#
#  Return an array of the k parts.
#
#
#  Example 1:
#
#
# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a
# ListNode is [].
#
#
#  Example 2:
#
#
# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1
# , and earlier parts are a larger size than the later parts.
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is in the range [0, 1000].
#  0 <= Node.val <= 1000
#  1 <= k <= 50
#
#
#  Related Topics Linked List 👍 3980 👎 318


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        if head is None:
            return [None for _ in range(k)]

        length = 0
        node = head
        while node is not None:
            node = node.next
            length += 1

        remain = length % k
        quotient = length // k

        length_list = [quotient + 1 for _ in range(remain)] + [quotient for _ in range(k-remain)]

        result = list()
        part_idx = 0
        node = head
        pre_node = None

        while len(result) != k:

            result.append(node)
            for _ in range(length_list[part_idx]):
                if node is not None:
                    pre_node = node
                    node = node.next

            pre_node.next = None
            part_idx += 1

        return result

# leetcode submit region end(Prohibit modification and deletion)
