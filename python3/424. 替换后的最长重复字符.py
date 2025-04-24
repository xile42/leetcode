class Solution:

    def characterReplacement(self, s: str, k: int) -> int:

        c = Counter()
        ans = left = 0
        for right in range(len(s)):
            c[s[right]] += 1
            while right - left + 1 - max(c.values()) > k:
                c[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans
