max = lambda a, b: a if a > b else b
min = lambda a, b: a if a < b else b


class Solution:

    def popcountDepth(self, n: int, k: int) -> int:

        def count(n, c):

            if c == 0:
                return 0
            bits = bin(n)[2:]
            m = len(bits)
            if c > m:
                return 0

            dp = [[[-1] * 2 for _ in range(c + 1)] for _ in range(m)]

            def dfs(pos, cnt, limit):

                if pos == m:
                    return 1 if cnt == c else 0

                if dp[pos][cnt][limit] != -1:
                    return dp[pos][cnt][limit]

                res = 0
                up = int(bits[pos]) if limit else 1
                for d in range(0, up + 1):
                    new_cnt = cnt + (1 if d == 1 else 0)
                    if new_cnt > c:
                        continue
                    new_limit = limit and (d == up)
                    res += dfs(pos + 1, new_cnt, new_limit)
                dp[pos][cnt][limit] = res

                return res

            return dfs(0, 0, True)

        max_bits = len(bin(n)[2:])

        if k == 0:
            return 1

        if k == 1:
            return count(n, 1) - 1

        if k == 2:
            ans = 0
            for c in [2, 4, 8, 16, 32]:
                if c <= max_bits:
                    ans += count(n, c)
            return ans

        if k == 3:
            ans = 0
            for x2 in [2, 4]:
                for x1 in range(2, min(50, max_bits) + 1):
                    if bin(x1).count('1') == x2:
                        ans += count(n, x1)
            return ans

        if k == 4:
            ans = 0
            for x2 in [3, 5]:
                for x1 in range(3, min(50, max_bits) + 1):
                    if bin(x1).count('1') == x2:
                        ans += count(n, x1)
            return ans

        return 0
