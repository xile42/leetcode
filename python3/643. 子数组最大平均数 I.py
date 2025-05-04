class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:

        ans = -inf
        s = 0
        n = len(nums)
        for i in range(n):
            s += nums[i]
            if i - k >= 0:
                s -= nums[i - k]
            if i >= k - 1:
                ans = max(ans, s / k)

        return ans
