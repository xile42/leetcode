class Solution:

    def pondSizes(self, land: List[List[int]]) -> List[int]:

        m, n = len(land), len(land[0])
        vis = [[False] * n for _ in range(m)]

        def dfs(i, j):

            vis[i][j] = True

            ans = 1
            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i + 1, j + 1), (i + 1, j - 1), (i - 1, j + 1), (i - 1, j - 1):
                if 0 <= ii < m and 0 <= jj < n and land[ii][jj] == 0 and not vis[ii][jj]:
                    ans += dfs(ii, jj)

            return ans

        ans = list()
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and land[i][j] == 0:
                    ans.append(dfs(i, j))

        return sorted(ans)
