class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:

        pre = list(accumulate(cardPoints))
        suf = list(accumulate(cardPoints[::-1]))
        ans = -inf
        for i in range(k + 1):
            left = 0 if i == 0 else pre[i - 1]
            right = 0 if k - i == 0 else suf[k - i - 1]
            ans = max(ans, left + right)

        return ans
