class Solution:

    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:

        c1, c2 = Counter(reduce(add, source)), Counter(reduce(add, target))
        ans = sum(c1.values())
        for k, v in c1.items():
            ans -= min(v, c2[k])

        return ans
