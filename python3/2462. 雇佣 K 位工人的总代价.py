class Solution:

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        n = len(costs)
        h = list()
        i = candidates
        j = max(n - candidates - 1, candidates - 1)
        for idx in range(i):
            heappush(h, [costs[idx], idx, 0])
        for idx in range(j + 1, n):
            heappush(h, [costs[idx], idx, 1])

        ans = 0
        for _ in range(k):
            c, idx, t = heappop(h)
            ans += c
            if i <= j:
                if t == 0:
                    heappush(h, [costs[i], i, 0])
                    i += 1
                else:
                    heappush(h, [costs[j], j, 1])
                    j -= 1

        return ans
