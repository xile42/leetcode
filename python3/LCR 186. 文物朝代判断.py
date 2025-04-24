class Solution:

    def checkDynasty(self, places: List[int]) -> bool:

        sn = sorted(places)
        chance = sn.count(0)
        cnt = 0
        for a, b in pairwise(sorted([v for v in sn if v != 0])):
            if a == b:
                return False
            cnt += b - a - 1
        
        return chance >= cnt
