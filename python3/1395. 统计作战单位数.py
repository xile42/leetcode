class Solution:

    def numTeams(self, rating: List[int]) -> int:

        ans = 0
        n = len(rating)

        pre = [0] * n
        suf = [0] * n
        for i, v in enumerate(rating):
            for j in range(i):
                if rating[j] < v:
                    pre[i] += 1
            for j in range(i + 1, n):
                if rating[j] < v:
                    suf[i] += 1
        for i, v in enumerate(rating):
            ans += pre[i] * (n - 1 - i - suf[i]) + (i - pre[i]) * suf[i]

        return ans
