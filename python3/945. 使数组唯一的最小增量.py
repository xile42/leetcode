class Solution:

    def minIncrementForUnique(self, nums: List[int]) -> int:

        ans = 0
        ns = sorted(nums)
        cur = ns[0]
        for n in ns[1:]:
            v = max(cur + 1, n)
            ans += max(v - n, 0)
            cur = v

        return ans
