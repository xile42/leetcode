class Solution:

    def perfectPairs(self, nums: List[int]) -> int:

        ns = sorted(abs(x) for x in nums)
        n = len(ns)
        ans = j = 0
        for i in range(n):
            if j <= i:
                j = i + 1
            while j < n and ns[j] <= 2 * ns[i]:
                j += 1
            ans += j - i - 1

        return ans
