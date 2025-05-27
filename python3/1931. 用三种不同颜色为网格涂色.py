class Solution:

    def colorTheGrid(self, m: int, n: int) -> int:

        pow3 = [3 ** i for i in range(m)]
        valid = []
        for color in range(3 ** m):
            for i in range(1, m):
                if color // pow3[i] % 3 == color // pow3[i - 1] % 3:  # 相邻颜色相同
                    break
            else:  # 没有中途 break，合法
                valid.append(color)

        nv = len(valid)
        nxt = [[] for _ in range(nv)]
        for i, color1 in enumerate(valid):
            for j, color2 in enumerate(valid):
                for p3 in pow3:
                    if color1 // p3 % 3 == color2 // p3 % 3:  # 相邻颜色相同
                        break
                else:  # 没有中途 break，合法
                    nxt[i].append(j)

        MOD = 1_000_000_007

        @cache
        def dfs(i: int, j: int) -> int:

            if i == 0:
                return 1

            return sum(dfs(i - 1, k) for k in nxt[j]) % MOD

        return sum(dfs(n - 1, j) for j in range(nv)) % MOD

# class Solution:
#
#     def colorTheGrid(self, m: int, n: int) -> int:
#
#         base = 10 ** 9 + 7
#         grid = [[-1 for _ in range(n)] for _ in range(m)]
#         colors = ["r", "g", "b"]
#
#         def check(i, j):
#
#             s = set()
#             if i - 1 >= 0:
#                 s.add(grid[i - 1][j])
#             if j - 1 >= 0:
#                 s.add(grid[i][j - 1])
#
#             return s
#
#         def f(i, j):
#
#             if i == m:
#                 return 1
#
#             # 遍历所有情况，超时
#             ans = 0
#             used = check(i, j)
#             for c in colors:
#                 if c in used:
#                     continue
#                 grid[i][j] = c
#                 if j == n - 1:
#                     ans += f(i + 1, 0) % base
#                 else:
#                     ans += f(i, j + 1) % base
#                 grid[i][j] = -1
#
#             return ans % base
#
#
#         ans = f(0, 0)
#
#         return ans
