class Solution:

    def maximumStrongPairXor(self, nums: List[int]) -> int:

        ans = 0
        n = len(nums)
        for i in range(n):
            a = nums[i]
            for j in range(i + 1, n):
                b = nums[j]
                if abs(a - b) <= min(a, b):
                    ans = max(ans, a ^ b)

        return ans
