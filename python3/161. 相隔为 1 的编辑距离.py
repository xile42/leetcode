class Solution:

    def isOneEditDistance(self, s: str, t: str) -> bool:

        s, t = (t, s) if len(t) < len(s) else (s, t)
        m, n = len(s), len(t)

        if not n - m <= 1:
            return False

        for idx in range(m):
            if s[idx] != t[idx]:
                if m == n:
                    return s[idx+1:] == t[idx+1:]
                else:
                    return s[idx:] == t[idx+1:]

        if m != n:
            return True
        else:
            return False


##        m, n = len(s), len(t)
##        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
##
##        for i in range(m+1):
##            dp[i][0] = i
##        for i in range(n+1):
##            dp[0][i] = i
##
##        for i in range(1, m+1):
##            for j in range(1, n+1):
##                if s[i-1] == t[j-1]:
##                    dp[i][j] = dp[i-1][j-1]
##                else:
##                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
##
##        return dp[m][n] == 1
