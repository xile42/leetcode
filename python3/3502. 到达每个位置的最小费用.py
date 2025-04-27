class Solution:

    def minCosts(self, cost: List[int]) -> List[int]:

        n = len(cost)
        pre = [inf] * n
        pre[0] = cost[0]
        for i in range(1, n):
            pre[i] = min(pre[i - 1], cost[i])

        ans = [inf] * n
        for i in range(n):
            if i == 0:
                ans[i] = cost[i]
            else:
                ans[i] = min(pre[i - 1], cost[i])

        return ans
