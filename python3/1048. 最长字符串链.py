class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        words.sort(key=len, reverse=True)
        wordSet = set(words)

        @cache
        def f(s):

            if s not in wordSet:
                return 0

            ans = 0
            for i in range(len(s)):
                t = s[:i] + s[i + 1:]
                ans = max(ans, f(t) + 1)

            return ans

        ans = 0
        for s in words:
            ans = max(ans, f(s))

        return ans
