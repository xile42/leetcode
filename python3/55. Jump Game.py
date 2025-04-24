# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum jump
# length at that position.
#
#  Return true if you can reach the last index, or false otherwise.
#
#
#  Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
#  Example 2:
#
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁴
#  0 <= nums[i] <= 10⁵
#
#
#  Related Topics Array Dynamic Programming Greedy 👍 19538 👎 1260


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def canJump(self, nums: List[int]) -> bool:

        start, end = 0, 0
        visited = 0

        while start <= end < len(nums):
            for idx in range(start, end+1):
                if idx >= len(nums):
                    break
                end = max(end, min(idx+nums[idx], len(nums)-1))
            if end <= visited:
                break
            start = visited + 1
            visited = end

        return True if visited == len(nums)-1 else False

    # def canJump(self, nums: List[int]) -> bool:
    #
    #     dp = [float("inf") for _ in range(len(nums))]
    #     dp[0] = 0
    #
    #     for idx in range(0, len(nums)):
    #         for jdx in range(1, nums[idx]+1):
    #             if idx + jdx >= len(nums):
    #                 break
    #             dp[idx+jdx] = min(dp[idx+jdx], dp[idx]+1)
    #
    #     return True if dp[-1] != float("inf") else False

# leetcode submit region end(Prohibit modification and deletion)
