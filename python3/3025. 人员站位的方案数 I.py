class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:

        ans = 0
        n = len(points)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x, y = points[i]
                xx, yy = points[j]
                if not (x <= xx and y >= yy):
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    xxx, yyy = points[k]
                    if x <= xxx <= xx and yy <= yyy <= y:
                        break
                else:
                    ans += 1

        return ans
