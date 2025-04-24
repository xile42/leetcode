import math

class Solution:

    def calcu_dist(self, x, y, xx, yy):

        return math.sqrt(pow(x-xx, 2) + pow(y-yy, 2))

    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        results = list()
        for xx, yy, r in queries:
            count = 0
            for x, y in points:
                if self.calcu_dist(x, y, xx, yy) <= r:
                    count += 1
            results.append(count)

        return results
