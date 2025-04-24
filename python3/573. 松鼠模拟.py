class Solution:

    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:

        @cache
        def dist(x, y, x1, y1):
            return abs(x-x1) + abs(y-y1)

        result = 0
        tx, ty = tree
        for nx, ny in nuts:
            result += 2 * dist(nx, ny, tx, ty)

        sn_dist = list()
        sx, sy = squirrel
        for i, (nx, ny) in enumerate(nuts):
            sn_dist.append([i, dist(nx, ny, sx, sy) - dist(nx, ny, tx, ty)])
        sn_dist.sort(key=lambda x: x[-1])

        result += sn_dist[0][1]

        return result
