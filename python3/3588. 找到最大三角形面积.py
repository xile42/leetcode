class Solution:

    def maxArea(self, coords: List[List[int]]) -> int:

        mnx, mny = inf, inf
        mxx, mxy = -inf, -inf
        dmnx, dmny = defaultdict(lambda: inf), defaultdict(lambda: inf)
        dmxx, dmxy = defaultdict(lambda: -inf), defaultdict(lambda: -inf)
        cx, cy = Counter(), Counter()
        for x, y in coords:
            mnx, mny = min(mnx, x), min(mny, y)
            mxx, mxy = max(mxx, x), max(mxy, y)
            dmnx[y] = min(dmnx[y], x)
            dmxx[y] = max(dmxx[y], x)
            dmny[x] = min(dmny[x], y)
            dmxy[x] = max(dmxy[x], y)
            cx[x] += 1
            cy[y] += 1

        ans = 0
        for x in cx:
            if cx[x] > 1:
                ans = max(ans, (dmxy[x] - dmny[x]) * abs(mxx - x), (dmxy[x] - dmny[x]) * abs(mnx - x))
        for y in cy:
            if cy[y] > 1:
                ans = max(ans, (dmxx[y] - dmnx[y]) * abs(mxy - y), (dmxx[y] - dmnx[y]) * abs(mny - y))

        return ans if ans > 0 else -1
