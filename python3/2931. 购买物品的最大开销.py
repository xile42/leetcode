class Solution:

    def maxSpending(self, values: List[List[int]]) -> int:

        heaps = list()
        for row in values:
            heaps.append(row)
            heapify(heaps[-1])

        m, n = len(values), len(values[0])
        ans = 0
        candidates = [heappop(heaps[i]) for i in range(len(heaps))]
        for day in range(1, m * n + 1):
            min_v = inf
            min_idx = None
            for idx, value in enumerate(candidates):
                if value < min_v:
                    min_v = value
                    min_idx = idx
            ans += min_v * day
            candidates[min_idx] = inf if len(heaps[min_idx]) == 0 else heappop(heaps[min_idx])

        return ans
