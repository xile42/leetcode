class Solution:

    def minimumCost(self, cost: List[int]) -> int:

        sc = sorted(cost, reverse=True)
        idx = 0
        ans = 0
        while idx * 3 < len(sc):
            group = sc[idx * 3:(idx + 1) * 3]
            if len(group) < 3:
                ans += sum(group)
            else:
                ans += sum(group[:2])
            idx += 1

        return ans
