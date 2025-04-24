class Solution:

    def maximumScore(self, cards: List[int], cnt: int) -> int:

        ans = 0
        for i in permutations(cards, cnt):
            if not (s := sum(i)) & 1:
                ans = max(ans, s)

        return ans
