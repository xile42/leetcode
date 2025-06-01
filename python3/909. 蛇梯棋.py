from collections import deque


class Solution:

    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        d = dict()

        cur = 1
        x, y = n - 1, 0
        while True:
            if y == 0:
                while y != n:
                    d[cur] = [x, y]
                    cur += 1
                    y += 1
                y = n - 1
            else:
                while y != -1:
                    d[cur] = [x, y]
                    cur += 1
                    y -= 1
                y = 0
            x -= 1
            if x == -1:
                break

        q = set()
        q.add(1)
        ans = 0
        vis = [False] * (n * n + 1)
        while q:
            next_q = set()
            for i in q:
                if i == n * n:
                    return ans
                for j in range(i + 1, min(i + 6, n * n) + 1):
                    x, y = d[j]
                    v = board[x][y]
                    tar = j if v == -1 else v
                    if not vis[tar]:
                        vis[tar] = True
                        next_q.add(tar)
            q = next_q
            ans += 1

        return -1
