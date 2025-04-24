class Solution:

    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:

        ans = list()
        h = list()
        for x, y in queries:
            d = abs(x) + abs(y)
            heappush(h, -d)
            if len(h) < k:
                ans.append(-1)
                continue

            if len(h) > k:
                heappop(h)
            ans.append(-h[0])

        return ans
