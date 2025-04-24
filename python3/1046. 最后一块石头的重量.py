class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:

        h = [-v for v in stones]
        heapify(h)

        while len(h) > 1:
            a = -heappop(h)
            b = -heappop(h)
            if a == b:
                continue
            else:
                heappush(h, b - a)

        return 0 if not h else -h[0]
