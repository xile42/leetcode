class Solution:

    def minOperations(self, nums: List[int]) -> int:

        ans = 0
        cur = nums[0]

        for n in nums[1:]:
            ans += max(cur + 1 - n, 0)
            cur = max(n, cur + 1)

        return ans
