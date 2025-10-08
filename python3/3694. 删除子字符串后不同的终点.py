class Solution:

    def distinctPoints(self, s: str, k: int) -> int:

        n = len(s)
        d = {
            "U": [0, 1],
            "D": [0, -1],
            "L": [-1, 0],
            "R": [1, 0],
        }

        total_x, total_y = 0, 0
        for c in s:
            dx, dy = d[c]
            total_x += dx
            total_y += dy

        pre_x = [0] * (n + 1)
        pre_y = [0] * (n + 1)
        for i, c in enumerate(s):
            dx, dy = d[c]
            pre_x[i + 1] = pre_x[i] + dx
            pre_y[i + 1] = pre_y[i] + dy

        vis = set()
        for i in range(0, n - k + 1):
            x_to_sub = pre_x[i + k] - pre_x[i]
            y_to_sub = pre_y[i + k] - pre_y[i]
            x = total_x - x_to_sub
            y = total_y - y_to_sub
            vis.add((x, y))

        return len(vis)
