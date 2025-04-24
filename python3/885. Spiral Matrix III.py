class Solution:

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        from collections import defaultdict

        dir = 0  # 0-r 1-d 2-l 3-u
        next_dir = 1
        dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visit = defaultdict(lambda: False)
        results = list()
        x, y = rStart, cStart

        results.append([x, y])
        visit[(x, y)] = True
        dx, dy = dxy[dir]
        x, y = x + dx, y + dy
        while len(results) < rows * cols:

            if 0 <= x < rows and 0 <= y <cols:
                visit[(x, y)] = True
                results.append([x, y])

            dx, dy = dxy[next_dir]
            xx, yy = x + dx, y + dy
            if not visit[(xx, yy)]:
                x, y = xx, yy
                dir = next_dir
                next_dir = 0 if next_dir == 3 else next_dir + 1
            else:
                dx, dy = dxy[dir]
                x, y = x + dx, y + dy

        return results
