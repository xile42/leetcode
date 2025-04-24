class Solution:

    def pathsWithMaxScore(self, board: List[str]) -> List[int]:

        base = pow(10, 9) + 7
        m, n = len(board), len(board[0])
        dp = [[Counter() for _ in range(n)] for _ in range(m)]
        value = {str(i): i for i in range(1, 10)}
        value["E"] = 0
        value["S"] = 0

        dp[0][0][0] += 1
        for i in range(n):
            if board[0][i] == "X":
                continue
            vij = value[board[0][i]]
            for v, cnt in dp[0][i - 1].items():
                dp[0][i][v + vij] += cnt % base
        for i in range(m):
            if board[i][0] == "X":
                continue
            vij = value[board[i][0]]
            for v, cnt in dp[i - 1][0].items():
                dp[i][0][v + vij] += cnt % base

        for i in range(1, m):
            for j in range(1, n):
                if board[i][j] == "X":
                    continue
                vij = value[board[i][j]]
                # for v, cnt in dp[i - 1][j].items():
                #     dp[i][j][v + vij] += cnt % base
                # for v, cnt in dp[i][j - 1].items():
                #     dp[i][j][v + vij] += cnt % base
                # for v, cnt in dp[i - 1][j - 1].items():
                #     dp[i][j][v + vij] += cnt % base
                ks = list(dp[i - 1][j].keys()) + list(dp[i][j - 1].keys()) + list(dp[i - 1][j - 1].keys())
                if not ks:
                    continue
                mx_k = max(ks)
                mx_v = dp[i - 1][j][mx_k] + dp[i][j - 1][mx_k] + dp[i - 1][j - 1][mx_k]
                dp[i][j][mx_k + vij] += mx_v % base

        if len(dp[-1][-1]) == 0:
            return [0, 0]

        mx_k = max(dp[-1][-1].keys()) % base
        mx_v = dp[-1][-1][mx_k] % base

        return [mx_k, mx_v]
