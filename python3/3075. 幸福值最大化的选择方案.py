class Solution:

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        ns = sorted(happiness)[-k:]
        ans = 0
        for i, n in enumerate(ns[::-1]):
            v = max(n - i, 0)
            ans += v

        return ans
