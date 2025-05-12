class Solution:

    def subArrayRanges(self, nums: List[int]) -> int:

        ans = 0
        n = len(nums)
        for i in range(n):
            mx, mn = nums[i], nums[i]
            for j in range(i, n):
                cur = nums[j]
                mn = min(mn, cur)
                mx = max(mx, cur)
                ans += mx - mn

        return ans
