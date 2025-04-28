class Solution:

    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        x_mn = defaultdict(lambda: inf)
        y_mn = defaultdict(lambda: inf)
        x_mx = defaultdict(lambda: -inf)
        y_mx = defaultdict(lambda: -inf)

        for x, y in buildings:
            x_mn[y] = min(x_mn[y], x)
            x_mx[y] = max(x_mx[y], x)
            y_mn[x] = min(y_mn[x], y)
            y_mx[x] = max(y_mx[x], y)

        ans = 0
        for x, y in buildings:
            if x_mn[y] < x < x_mx[y] and y_mn[x] < y < y_mx[x]:
                ans += 1

        return ans
