class Solution:

    def minKnightMoves(self, x: int, y: int) -> int:

        if x == 0 and y == 0:
            return 0

        tx, ty = abs(x), abs(y)
        x_max, y_max = tx + 5, ty + 5

        q = list()
        q.append((0, 0))
        step = 0
        vis = set()
        while True:
            step += 1
            next_q = list()
            while q:
                x, y = q.pop(0)
                for xx, yy in (x + 1, y + 2), (x + 2, y + 1), (x + 1, y - 2), (x + 2, y - 1), (x - 1, y - 2), (x - 2, y - 1), (x - 2, y + 1), (x - 1, y + 2):
                    if not (-5 <= xx <= x_max and -5 <= yy <= y_max):
                        continue
                    if xx == tx and yy == ty:
                        return step
                    if (xx, yy) not in vis:
                        vis.add((xx, yy))
                        next_q.append((xx, yy))
            q = next_q
