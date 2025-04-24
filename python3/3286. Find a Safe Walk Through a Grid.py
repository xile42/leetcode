from typing import List


class Solution:

    def adj_ij(self, x, y):

        results = list()
        dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dx, dy in dxy:
            xx, yy = x + dx, y + dy
            if 0 <= xx < self.m and 0 <= yy < self.n:
                results.append([xx, yy])

        return results

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        self.m, self.n = len(grid), len(grid[0])
        dp = [[-float("inf") for _ in range(self.n)] for _ in range(self.m)]
        queue = list()
        queue.append([0, 0])
        dp[0][0] = health - grid[0][0]

        while len(queue) != 0 and dp[-1][-1] <= 0:
            x, y = queue.pop(0)
            for xx, yy in self.adj_ij(x, y):
                dp_value = dp[x][y] - grid[xx][yy]
                if dp_value <= dp[xx][yy]:
                    continue
                dp[xx][yy] = dp_value
                if dp[xx][yy] > 0:
                    queue.append([xx, yy])

        return True if dp[-1][-1] > 0 else False


if __name__ == '__main__':

    foo = Solution()
    result = foo.findSafeWalk([[1, 1, 1, 1]], 4)
    print(result)
