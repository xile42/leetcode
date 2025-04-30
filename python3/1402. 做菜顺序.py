class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        ns = sorted(satisfaction)
        n = len(ns)

        @cache
        def f(i, factor):

            if i >= n:
                return 0

            if ns[i] >= 0:
                return f(i + 1, factor + 1) + ns[i] * factor
            else:
                return max(f(i + 1, factor + 1) + ns[i] * factor, f(i + 1, factor))

        return f(0, 1)
