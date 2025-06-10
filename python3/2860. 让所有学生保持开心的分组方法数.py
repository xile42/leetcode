class Solution:

    def countWays(self, nums: List[int]) -> int:

        ns = sorted(nums)
        ans = 0

        if ns[0] > 0:
            ans += 1

        for left in range(len(ns) - 1):
            l = left + 1
            if l > ns[left] and l < ns[left + 1]:
                ans += 1

        if len(nums) > ns[-1]:
            ans += 1

        return ans
