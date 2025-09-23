class Solution:

    def isRobotBounded(self, s: str) -> bool:

        x, y, d = 0, 0, 0
        dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        for c in s:
            if c == "G":
                x += dirs[d][0]
                y += dirs[d][1]
            elif c == "L":
                d = (d + 1) % 4
            else:
                d = ((d - 1) % 4 + 4) % 4

        return (x == 0 and y == 0) or d != 0
