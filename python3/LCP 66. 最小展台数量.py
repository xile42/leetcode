class Solution:

    def minNumBooths(self, demand: List[str]) -> int:

        c = reduce(or_, [Counter(i) for i in demand])

        return sum(c.values())
