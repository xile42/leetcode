class Solution:

    def maximumProduct(self, nums: List[int], m: int) -> int:

        n = len(nums)

        mn = [inf] * n
        mx = [-inf] * n
        mn[0] = nums[0]
        mx[0] = nums[0]
        for i in range(1, n):
            mn[i] = min(mn[i - 1], nums[i])
            mx[i] = max(mx[i - 1], nums[i])

        ans = -inf
        for right in range(m - 1, n):
            v = nums[right]
            ans = max(ans, v * mn[right - m + 1], v * mx[right - m + 1])

        return ans
