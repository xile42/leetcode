class Solution:

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = list()
        potions.sort()
        vs = [success / i for i in spells]
        for v in vs:
            ans.append(len(potions) - bisect_left(potions, v))

        return ans
