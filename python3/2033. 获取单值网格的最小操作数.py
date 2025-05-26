class Solution:

    def minOperations(self, grid: List[List[int]], x: int) -> int:

        ns = list()
        for row in grid:
            ns += row
        n = len(ns)
        ns.sort()

        ans = 0
        tar = ns[(n - 1) // 2]
        for v in ns:
            if abs(v - tar) % x != 0:
                return -1
            ans += abs(v - tar) // x

        return ans
