# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
#
#
#  Example 1:
#  Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#  Example 2:
#  Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#
#  Example 3:
#  Input: nums = [1]
# Output: [[1]]
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 6
#  -10 <= nums[i] <= 10
#  All the integers of nums are unique.
#
#
#  Related Topics Array Backtracking 👍 19181 👎 330


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    result = list()

    def search(self, nums, current):

        if len(nums) == 0:
            self.result.append(current)

        for idx, num in enumerate(nums):
            self.search(nums[:idx]+nums[idx+1:], current+[num])

    def permute(self, nums: List[int]) -> List[List[int]]:

        self.result = list()
        self.search(nums, list())
        return self.result

# leetcode submit region end(Prohibit modification and deletion)
