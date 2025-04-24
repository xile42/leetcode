class Solution:

    def minCount(self, coins: List[int]) -> int:

        return sum(ceil(i / 2) for i in coins)
