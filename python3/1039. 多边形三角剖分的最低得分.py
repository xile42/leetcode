class Solution:

    def minScoreTriangulation(self, v: List[int]) -> int:

        @cache
        def dfs(i: int, j: int) -> int:
            if i + 1 == j:
                return 0
            return min(dfs(i, k) + dfs(k, j) + v[i] * v[j] * v[k] for k in range(i + 1, j))

        return dfs(0, len(v) - 1)
