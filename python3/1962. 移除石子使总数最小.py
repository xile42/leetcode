class Solution:

    def minStoneSum(self, piles: List[int], k: int) -> int:

        piles = [-i for i in piles]
        heapify(piles)
        for _ in range(k):
            v = -heappop(piles)
            heappush(piles, -(v - floor(v / 2)))

        return -sum(piles)
