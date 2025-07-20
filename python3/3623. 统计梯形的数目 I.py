class Solution:

    def countTrapezoids(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x: x[1])
        ans = 0
        base = 10 ** 9 + 7
        cur = before = 0
        last_y = None

        for x, y in points:
            if y != last_y:
                before += cur * (cur - 1) // 2
                cur = 1
                last_y = y
            else:
                cur += 1
                choices = cur - 1
                ans += (choices * before) % base
                ans %= base

        return ans
