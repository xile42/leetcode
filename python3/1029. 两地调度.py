class Solution:

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        n = len(costs) // 2
        ans = sum([i[0] for i in costs])
        diff = [i[1] - i[0] for i in costs]
        diff.sort()

        return ans + sum(diff[:n])
