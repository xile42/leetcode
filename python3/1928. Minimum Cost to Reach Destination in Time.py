class Solution:
    def minCost(
        self, maxTime: int, edges: List[List[int]], passingFees: List[int]
    ) -> int:
        m, n = maxTime, len(passingFees)
        f = [[inf] * n for _ in range(m + 1)]
        f[0][0] = passingFees[0]
        for i in range(1, m + 1):
            for x, y, t in edges:
                if t <= i:
                    f[i][x] = min(f[i][x], f[i - t][y] + passingFees[x])
                    f[i][y] = min(f[i][y], f[i - t][x] + passingFees[y])
        ans = min(f[i][n - 1] for i in range(m + 1))
        return ans if ans < inf else -1


# from collections import defaultdict
#
#
# class Solution:
#
#     results = None
#
#     def search(self, start, target, current_time, current_cost, visit):
#         # print(start, target, current_time, current_cost)
#         if start == target:
#             self.results.append(current_cost)
#             return
#
#         queue = list()
#         _visit = visit.copy()
#         for next_node in self.graph[start]:
#             next_time = self.graph[start][next_node]
#             next_cost = self.costs[next_node]
#             time = current_time + next_time
#             if time > self.max_time:
#                 continue
#             if time >= visit[next_node]:
#                 continue
#             _visit[next_node] = time
#             queue.append([next_node, time, current_cost+next_cost])
#         visit = _visit
#
#         for _start, time, cost in queue:
#             self.search(_start, target, time, cost, visit)
#
#     def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
#
#         self.max_time = maxTime
#         self.n = len(passingFees)
#         self.costs = passingFees
#         self.graph = defaultdict(lambda: defaultdict(lambda: float("inf")))
#         for i, j, t in edges:
#             self.graph[i][j] = min(self.graph[i][j], t)
#             self.graph[j][i] = min(self.graph[j][i], t)
#
#         self.results = list()
#         visit = defaultdict(lambda: float("inf"))
#         visit[0] = 0
#         self.search(0, self.n-1, 0, self.costs[0], visit)
#
#         return -1 if len(self.results) == 0 else min(self.results)
