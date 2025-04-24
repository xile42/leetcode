# Given an integer array nums of unique elements, return all possible subsets (
# the power set).
#
#  The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
#  Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
#  Example 2:
#
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10
#  -10 <= nums[i] <= 10
#  All the numbers of nums are unique.
#
#
#  Related Topics Array Backtracking Bit Manipulation 👍 17405 👎 284


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    result = None

    def search(self, candidates, current):

        self.result.append(current)

        for idx, num in enumerate(candidates):
            self.search(candidates[idx+1:], current+[num])

    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.result = list()
        self.search(nums, list())

        return self.result

# leetcode submit region end(Prohibit modification and deletion)
