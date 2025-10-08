class Solution:

    def countStableSubsequences(self, nums: List[int]) -> int:

        ns = [n & 1 for n in nums]
        base = 10 ** 9 + 7
        n = len(ns)

        @cache
        def f(i, pre2, pre1):

            if i >= n:
                if pre2 == -inf and pre1 == -inf:
                    return 0
                else:
                    return 1

            v = ns[i]
            cur = v + pre1 + pre2
            ans = 0
            ans += f(i + 1, pre2, pre1) % base
            if cur != 0 and cur != 3:
                ans += f(i + 1, pre1, v) % base

            return ans % base

        ans = f(0, -inf, -inf)
        f.cache_clear()

        return ans % base
