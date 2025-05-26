class Solution:

    def sumOfBeauties(self, nums: List[int]) -> int:

        n = len(nums)
        pre_mx = [-inf] * n
        pre_mx[0] = nums[0]
        for i in range(1, n):
            pre_mx[i] = max(pre_mx[i - 1], nums[i])
        suf_mn = [inf] * n
        suf_mn[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf_mn[i] = min(suf_mn[i + 1], nums[i])

        ans = 0
        for i in range(1, n - 1):
            v = nums[i]
            if pre_mx[i - 1] < v and v < suf_mn[i + 1]:
                ans += 2
            elif nums[i - 1] < v < nums[i + 1]:
                ans += 1

        return ans
