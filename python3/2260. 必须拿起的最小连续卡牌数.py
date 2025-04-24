class Solution:

    def minimumCardPickup(self, cards: List[int]) -> int:

        ans = inf
        d = dict()
        for i, v in enumerate(cards):
            if v in d:
                ans = min(ans, i - d[v] + 1)
            d[v] = i

        return -1 if ans == inf else ans
