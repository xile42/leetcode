class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        s.sort()
        g.sort()
        idx = 0
        n = len(g)
        for x in s:
            if idx < n and x >= g[idx]:
                idx += 1

        return idx
