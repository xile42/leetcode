class Solution:

    def pickGifts(self, gifts: List[int], k: int) -> int:

        gifts = [-i for i in gifts]
        heapify(gifts)
        for _ in range(k):
            v = -heappop(gifts)
            heappush(gifts, -isqrt(v))

        return -sum(gifts)
