class Solution:

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        ans = left = 0
        cnt = Counter()
        for right, n in enumerate(answerKey):
            cnt[n] += 1
            while min(cnt["T"], cnt["F"]) > k:
                cnt[answerKey[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans
