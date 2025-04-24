class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:

        m, n = len(points), len(points[0])
        dp = [[-inf for _ in range(n)] for _ in range(m)]
        
        pre = [-inf for _ in range(n)]
        suf = [-inf for _ in range(n)]
        for i in range(n):
            dp[0][i] = points[0][i]
            if i == 0:
                pre[i] = dp[0][i] + i
            else:
                pre[i] = max(pre[i - 1], dp[0][i] + i)
        suf[n - 1] = dp[0][n - 1] - (n - 1)
        for i in range(n - 2, -1, -1):
            suf[i] = max(suf[i + 1], dp[0][i] - i)
        
        for i in range(1, m):
            for j in range(n):
                v1 = points[i][j] - j + pre[j]
                v2 = points[i][j] + j + (-inf if j + 1 >= n else suf[j + 1])
                dp[i][j] = max(v1, v2)
                
            pre[0] = dp[i][0] + 0
            for k in range(1, n):
                pre[k] = max(pre[k - 1], dp[i][k] + k)
            suf[-1] = dp[i][-1] - (n - 1)
            for k in range(n - 2, -1, -1):
                suf[k] = max(suf[k + 1], dp[i][k] - k)

        return max(dp[-1])
