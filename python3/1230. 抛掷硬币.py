class Solution:

    def probabilityOfHeads(self, prob: List[float], target: int) -> float:

        p1 = prob
        p0 = [1 - p for p in prob]
        n = len(prob)
        m = target

        @cache
        def f(i, left):

            if i >= n:
                return 1 if left == 0 else 0

            if left:
                return p1[i] * f(i + 1, left - 1) + p0[i] * f(i + 1, left)
            else:
                return p0[i] * f(i + 1, left)

        return f(0, m)
