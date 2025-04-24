class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:

        c = Counter()
        for x, y in points:
            if x == 0:
                c[(0, inf)] += 1
            if y == 0:
                c[(inf, 0)] += 1
            if x != 0 and y != 0:
                k = gcd(x, y)
                c[(x // k, y // k)] += 1

        return max(c.values())
