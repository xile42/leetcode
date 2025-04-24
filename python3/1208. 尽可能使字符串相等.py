class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        ans = left = 0
        cur = 0
        for right, c in enumerate(t):
            cur += abs(ord(c) - ord(s[right]))
            while cur > maxCost:
                cur -= abs(ord(t[left]) - ord(s[left]))
                left += 1
            ans = max(ans, right - left + 1)

        return ans
