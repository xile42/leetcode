class Solution:

    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m, n = len(grid), len(grid[0])
        ans = [[0 for _ in range(n - k + 1)] for _ in range(m - k + 1)]

        for i in range(m - k + 1):

            s = SortedSet()
            c = Counter()

            for j in range(n - k + 1):

                if j == 0:
                    for ii in range(i, i + k):
                        for jj in range(j, j + k):
                            v = grid[ii][jj]
                            c[v] += 1
                            s.add(v)

                else:
                    for ii in range(i, i + k):
                        v = grid[ii][j + k - 1]
                        c[v] += 1
                        s.add(v)
                    for ii in range(i, i + k):
                        v = grid[ii][j - 1]
                        c[v] -= 1
                        if c[v] == 0:
                            del c[v]
                            s.remove(v)

                if len(s) == 1:
                    ans[i][j] = 0
                else:
                    ans[i][j] = min(b - a for a, b in pairwise(s))

        return ans
