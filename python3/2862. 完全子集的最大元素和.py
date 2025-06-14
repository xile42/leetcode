class Solution:

    def maximumSum(self, nums: List[int]) -> int:

        n = len(nums)
        ans = cur = 0
        for i in range(1, n + 1):
            for j in count(1):
                if (v := i * j * j - 1) < n:
                    cur += nums[v]
                else:
                    break
            ans = max(ans, cur)
            cur = 0

        return ans
