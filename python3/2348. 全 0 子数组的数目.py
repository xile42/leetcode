class Solution:

    def zeroFilledSubarray(self, nums: List[int]) -> int:

        ans = 0
        for c, ite in groupby(nums):
            if c == 0:
                l = len(list(ite))
                ans += l * (l + 1) // 2

        return ans
