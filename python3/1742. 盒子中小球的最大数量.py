class Solution:

    def countBalls(self, lowLimit: int, highLimit: int) -> int:

        c = Counter()
        for n in range(lowLimit, highLimit + 1):
            c[sum(map(int, str(n)))] += 1

        return max(c.values())
