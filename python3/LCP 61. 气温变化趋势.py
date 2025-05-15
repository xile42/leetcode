class Solution:

    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:

        a = [0 if b == a else (1 if b > a else -1) for a, b in pairwise(temperatureA)]
        b = [0 if b == a else (1 if b > a else -1) for a, b in pairwise(temperatureB)]
        c = [ai == bi for ai, bi in zip(a, b)]

        return max([0 if c == False else len(list(ite)) for c, ite in groupby(c)])
