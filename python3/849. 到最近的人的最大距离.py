class Solution:

    def maxDistToClosest(self, seats: List[int]) -> int:

        ans = 0
        groups = [[n, len(list(ite))] for n, ite in groupby(seats)]
        for i, (n, l) in enumerate(groups):
            if n == 0:
                if i == 0 or i == len(groups) - 1:
                    ans = max(ans, l)
                else:
                    ans = max(ans, (l // 2 + 1) if l & 1 else (l // 2))

        return ans
