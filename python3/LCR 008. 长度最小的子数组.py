class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        ans = inf
        left = 0
        n = len(nums)
        cur = 0
        for right in range(n):
            cur += nums[right]
            while cur - nums[left] >= target:
                cur -= nums[left]
                left += 1
            if cur >= target:
                ans = min(ans, right - left + 1)

        return ans if ans < inf else 0
