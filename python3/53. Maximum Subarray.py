### Given an integer array nums, find the subarray with the largest sum, and
### return its sum.
###
###
###  Example 1:
###
###
### Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
### Output: 6
### Explanation: The subarray [4,-1,2,1] has the largest sum 6.
###
###
###  Example 2:
###
###
### Input: nums = [1]
### Output: 1
### Explanation: The subarray [1] has the largest sum 1.
###
###
###  Example 3:
###
###
### Input: nums = [5,4,-1,7,8]
### Output: 23
### Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
###
###
###
###  Constraints:
###
###
###  1 <= nums.length <= 10⁵
###  -10⁴ <= nums[i] <= 10⁴
###
###
###
###  Follow up: If you have figured out the O(n) solution, try coding another
### solution using the divide and conquer approach, which is more subtle.
###
###  Related Topics Array Divide and Conquer Dynamic Programming 👍 34247 👎 1451
##
##
### leetcode submit region begin(Prohibit modification and deletion)
##class Solution:
##
##    def maxSubArray(self, nums: List[int]) -> int:
##
##        max_sum = -float("inf")
##        start = 0
##
##        while start < len(nums):
##
##            while start < len(nums) and nums[start] <= 0:
##                start += 1
##
##            this_sum = 0
##            this_max = -float("inf")
##            end = start
##            while end < len(nums):
##                value = nums[end]
##                if value > 0:
##                    this_sum += value
##                    this_max = max(this_max, this_sum)
##                elif this_sum + value > 0:
##                    this_sum += value
##                else:
##                    break
##                end += 1
##
##            max_sum = max(max_sum, this_max)
##            start = end + 1
##
##        if max_sum == -float("inf"):
##            return max(nums)
##
##        return max_sum
##
### leetcode submit region end(Prohibit modification and deletion)


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        dp = nums.copy()
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i - 1] + nums[i])

        return max(dp)

















