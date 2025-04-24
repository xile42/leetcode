class Solution:

    def maxCoins(self, piles: List[int]) -> int:

        sorted_piles = sorted(piles)
        result = 0

        idx = len(sorted_piles) - 2
        for _ in range(len(piles) // 3):
            result += sorted_piles[idx]
            idx -= 2

        return result
