class Solution:

    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:

        n = len(capacity)
        ns = sorted([capacity[i] - rocks[i] for i in range(n)])
        ans = 0
        idx = 0
        while idx < n and ns[idx] <= additionalRocks:
            ans += 1
            additionalRocks -= ns[idx]
            idx += 1

        return ans
