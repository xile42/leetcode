class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:

        n = len(nums)
        mx_suf = [0] * n
        mx_suf[-1] = nums[-1]
        mn_suf = [0] * n
        mn_suf[-1] = nums[-1]
        for idx in range(n - 2, -1, -1):
            mx_suf[idx] = max(nums[idx], mx_suf[idx + 1])
            mn_suf[idx] = min(nums[idx], mn_suf[idx + 1])

        ans = -inf
        for idx in range(n - 2):
            for jdx in range(idx + 1, n - 1):
                v = nums[idx] - nums[jdx]
                if v >= 0:
                    ans = max(ans, v * mx_suf[jdx + 1])
                else:
                    ans = max(ans, v * mn_suf[jdx + 1])

        return max(ans, 0)
