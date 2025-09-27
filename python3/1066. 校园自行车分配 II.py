class Solution:

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        n, m = len(workers), len(bikes)

        @cache
        def dfs(s):

            i = s.bit_count()
            if i == n:
                return 0
            a, b = workers[i]

            return min(abs(x-a) + abs(y-b) + dfs(s | (1 << j)) for j, (x, y) in enumerate(bikes) if (s >> j) & 1 == 0)

        return dfs(0)
