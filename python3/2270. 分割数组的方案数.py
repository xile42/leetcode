class Solution:

    def waysToSplitArray(self, nums: List[int]) -> int:

        acc = list(accumulate(nums))
        half = acc[-1] / 2
        ans = 0
        for i in range(len(nums) - 1):
            if acc[i] >= half:
                ans += 1

        return ans
