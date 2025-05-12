class Solution:

    def shareCandies(self, candies: List[int], k: int) -> int:

        cnt = Counter(candies)
        ans = -inf
        for i, n in enumerate(candies):
            cnt[n] -= 1
            if cnt[n] == 0:
                del cnt[n]
            if i >= k:
                cnt[candies[i - k]] += 1
            if i >= k - 1:
                ans = max(ans, len(cnt))

        return ans
