class Solution:

    def nimGame(self, piles: List[int]) -> bool:

        return reduce(xor, piles) != 0
