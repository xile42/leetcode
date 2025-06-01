class Solution:

    def minMoves(self, classroom: List[str], energy: int) -> int:

        m, n = len(classroom), len(classroom[0])

        start_i, start_j = -1, -1
        garbage = list()
        for i in range(m):
            for j in range(n):
                v = classroom[i][j]
                if v == "S":
                    start_i, start_j = i, j
                elif v == "L":
                    garbage.append((i, j))

        if len(garbage) == 0:
            return 0

        d = {}
        for idx, (i, j) in enumerate(garbage):
            d[(i, j)] = idx

        target = (1 << len(garbage)) - 1
        dp = [[[[inf] * (1 << len(garbage)) for _ in range(energy + 1)] for __ in range(n)] for ___ in range(m)]
        dp[start_i][start_j][energy][0] = 0
        q = deque()
        q.append((start_i, start_j, energy, 0))

        while q:

            i, j, e, mask = q.popleft()
            step = dp[i][j][e][mask]
            if mask == target:
                return step

            if e == 0 and classroom[i][j] != "R":
                continue

            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):

                if ii < 0 or ii >= m or jj < 0 or jj >= n:
                    continue

                v = classroom[ii][jj]
                if v == "X":
                    continue

                if e > 0:

                    new_e = e - 1 if v != "R" else energy
                    new_mask = mask

                    if v == "L":
                        idx = d[(ii, jj)]
                        new_mask |= (1 << idx)

                    if step + 1 < dp[ii][jj][new_e][new_mask]:
                        dp[ii][jj][new_e][new_mask] = step + 1
                        if new_mask == target:
                            return step + 1
                        q.append((ii, jj, new_e, new_mask))

        return -1