class Solution:

    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:

        ans = list()
        d = {
            "U": [-1, 0],
            "D": [1, 0],
            "R": [0, 1],
            "L": [0, -1]
        }
        for i in range(len(s)):
            cmd = s[i:]
            x, y = startPos
            for j, op in enumerate(cmd):
                dx, dy = d[op]
                x += dx
                y += dy
                if not (0 <= x < n and 0 <= y < n):
                    ans.append(j)
                    break
            else:
                ans.append(len(cmd))

        return ans
