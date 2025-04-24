class Solution:

    def projectionArea(self, grid: List[List[int]]) -> int:

        from collections import defaultdict

        xy_count = 0
        x_map = defaultdict(int)
        y_map = defaultdict(int)

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                z = grid[x][y]
                xy_count += 1 if z != 0 else 0
                x_map[x] = max(x_map[x], z)
                y_map[y] = max(y_map[y], z)

        result = 0
        result += xy_count
        for v in x_map.values():
            result += v
        for v in y_map.values():
            result += v

        return result
