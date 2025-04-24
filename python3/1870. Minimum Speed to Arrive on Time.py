import math


class Solution:

    def check(self, v):

        result = 0
        for d in self.dist[:-1]:
            result += math.ceil(d / v)
        result += self.dist[-1] / v
        return True if result <= self.hour else False

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        self.n = len(dist)
        self.dist = dist
        self.hour = hour
        left, right = 1, pow(10, 10)
        results = list()
        while left <= right:
            mid = left + (right - left) // 2
            if self.check(mid):
                right = mid - 1
                results.append(mid)
            else:
                left = mid + 1

        return -1 if len(results) == 0 else min(results)
