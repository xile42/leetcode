class Solution:

    def longestSemiRepetitiveSubstring(self, s: str) -> int:

        ans = left = 0
        chance = 1
        for right, c in enumerate(s):
            if right > 0 and c == s[right - 1]:
                chance -= 1
            while chance < 0:
                if s[left] == s[left + 1]:
                    chance += 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans
