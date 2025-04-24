class Solution:

    def maxCoins(self, piles: List[int]) -> int:

        n = len(piles) // 3
        piles.sort()

        return sum(piles[-2 * n:][::2])
