class Solution:

    def paintingPlan(self, n: int, k: int) -> int:

        if k == 0 or k == n ** 2:
            return 1

        ans = 0
        for i in range(n):
            for j in range(n):
                if n * (i + j) - (i * j) == k:
                    ans += comb(n, i) * comb(n, j)

        return ans
