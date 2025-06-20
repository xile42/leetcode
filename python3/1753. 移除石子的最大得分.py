class Solution:

    def maximumScore(self, a: int, b: int, c: int) -> int:

        a, b, c = sorted([a, b, c])

        if a + b <= c:
            return a + b

        return c + (a + b - c) // 2
