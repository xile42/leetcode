class Solution:

    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:

        cnt = min(maxWeight // w, n * n)

        return cnt