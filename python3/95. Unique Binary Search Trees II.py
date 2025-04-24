# Given an integer n, return all the structurally unique BST's (binary search
# trees), which has exactly n nodes of unique values from 1 to n. Return the answer
# in any order.
#
#
#  Example 1:
#
#
# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]
# ]
#
#
#  Example 2:
#
#
# Input: n = 1
# Output: [[1]]
#
#
#
#  Constraints:
#
#
#  1 <= n <= 8
#
#
#  Related Topics Dynamic Programming Backtracking Tree Binary Search Tree
# Binary Tree 👍 7596 👎 529


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def search(self, i, j):

        if i == j:
            return [TreeNode(val=i)]

        results = list()
        nums = list(range(i, j+1))

        for root_idx in range(len(nums)):

            root_value = nums[root_idx]
            left_start, left_end = 0, root_idx-1
            right_start, right_end = root_idx+1, len(nums)-1

            left_results = [None] if left_end < left_start else self.search(nums[left_start], nums[left_end])
            right_results = [None] if right_end < right_start else self.search(nums[right_start], nums[right_end])

            for left_result in left_results:
                for right_result in right_results:
                    root = TreeNode(val=root_value)
                    root.left = left_result
                    root.right = right_result
                    results.append(root)

        return results

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        results = self.search(1, n)

        return results

# leetcode submit region end(Prohibit modification and deletion)
