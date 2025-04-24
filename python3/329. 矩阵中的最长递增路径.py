class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])

        @cache
        def f(i, j):

            if not (0 <= i < m and 0 <= j < n):
                return 0

            ans = 1
            for ii, jj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= ii < m and 0 <= jj < n and matrix[ii][jj] > matrix[i][j]:
                    ans = max(ans, f(ii, jj) + 1)

            return ans

        ans = 1
        for i in range(m):
            for j in range(n):
                ans = max(ans, f(i, j))

        return ans
