# from typing import List
# from functools import cache
# from itertools import accumulate
# from math import inf
#
#
# class Solution:
#
#     def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
#
#         m, n = len(grid), len(grid[0])
#         grid = [sorted(row, reverse=True) for row in grid]
#         # accs = [[] if limits[i] == 0 else list(accumulate(sorted(row[:limits[i]], reverse=True))) for i, row in enumerate(grid)]
#
#         @cache
#         def f(i, chance):
#
#             if chance == 0:
#                 return 0
#
#             if i >= m:
#                 return -inf
#
#             ans = 0
#             cur = 0
#             for take in range(min(limits[i], chance) + 1):
#                 if take == 0:
#                     value = 0
#                 else:
#                     cur += grid[i][take - 1]
#                     value = cur
#                 ans = max(ans, value + f(i + 1, chance - take))
#
#             return ans
#
#         ans = f(0, k)
#
#         return ans
#
#
# foo = Solution()
# print(foo.maxSum([[1,2],[3,4]], [1,2], 2))


class Solution:

    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:

        m, n = len(grid), len(grid[0])
        grid = [sorted(row, reverse=True) for row in grid]
        h = list()
        heapify(h)
        idxs = [1] * m
        for i in range(m):
            heappush(h, [-grid[i][0], i])
        ans = 0
        for _ in range(k):
            while True:
                v, idx = heappop(h)
                v = -v
                # print(v, idx)
                if idxs[idx] < n:
                    heappush(h, [-grid[idx][idxs[idx]], idx])
                    idxs[idx] += 1
                if limits[idx] > 0:
                    limits[idx] -= 1
                    ans += v
                    break
                else:
                    continue

        return ans
