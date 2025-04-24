class Solution:

    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:

        ans = 0
        for i in range(total // cost1 + 1):
            left = total - i * cost1
            ans += left // cost2 + 1

        return ans
