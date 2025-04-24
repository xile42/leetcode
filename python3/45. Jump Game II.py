# You are given a 0-indexed array of integers nums of length n. You are
# initially positioned at nums[0].
#
#  Each element nums[i] represents the maximum length of a forward jump from
# index i. In other words, if you are at nums[i], you can jump to any nums[i + j]
# where:
#
#
#  0 <= j <= nums[i] and
#  i + j < n
#
#
#  Return the minimum number of jumps to reach nums[n - 1]. The test cases are
# generated such that you can reach nums[n - 1].
#
#
#  Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
#
#
#  Example 2:
#
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁴
#  0 <= nums[i] <= 1000
#  It's guaranteed that you can reach nums[n - 1].
#
#
#  Related Topics Array Dynamic Programming Greedy 👍 14692 👎 592


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def jump(self, nums: List[int]) -> int:

        dp = [float("inf") for _ in range(len(nums))]
        dp[0] = 0

        to_visit = list()
        to_visit.append(0)
        while len(to_visit) != 0:
            next_to_visit = list()
            for idx in to_visit:
                step_max = nums[idx]
                for jdx in range(1, step_max+1):
                    if idx + jdx >= len(nums):
                        break
                    if dp[idx]+1 < dp[idx+jdx]:
                        dp[idx+jdx] = dp[idx] + 1
                        next_to_visit.append(idx+jdx)
            to_visit = next_to_visit

        return int(dp[-1])

# leetcode submit region end(Prohibit modification and deletion)
