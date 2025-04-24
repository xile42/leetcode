class Solution:

    def sumCounts(self, nums: List[int]) -> int:

        ans = 0
        for l in range(1, len(nums) + 1):
            for i in range(len(nums)):
                t = nums[i:i + l]
                if len(t) != l:
                    break
                ans += len(set(t)) ** 2

        return ans
