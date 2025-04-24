class Solution:

    def minTimeToType(self, word: str) -> int:

        cur = "a"
        ans = len(word)
        for c in word:
            ans += min(
                abs(ord(c) - ord(cur)),
                26 - abs(ord(c) - ord(cur))
            )
            cur = c

        return ans
