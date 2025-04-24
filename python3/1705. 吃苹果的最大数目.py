class Solution:

    def eatenApples(self, apples: List[int], days: List[int]) -> int:

        h = list()
        ans = 0
        for cur in count(0):

            while h and (h[0][0] <= cur or h[0][1] <= 0):
                heappop(h)

            if cur < len(apples) and apples[cur] > 0:
                heappush(h, [cur + days[cur], apples[cur]])

            if len(h) == 0 and cur >= len(apples):
                return ans

            if len(h) == 0:
                continue

            h[0][1] -= 1
            ans += 1
