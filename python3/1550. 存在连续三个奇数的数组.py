class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        ns = [i & 1 for i in arr]
        for c, ite in groupby(ns):
            if c == 1 and len(list(ite)) >= 3:
                return True

        return False
