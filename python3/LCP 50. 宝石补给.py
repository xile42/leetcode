class Solution:

    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:

        for i, j in operations:
            num = floor(gem[i] / 2)
            gem[i] -= num
            gem[j] += num

        gem = sorted(gem)
        return gem[-1] - gem[0]
