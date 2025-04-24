class Solution:

    def numberOfSpecialSubstrings(self, s: str) -> int:

        ans = left = 0
        c = Counter()
        for right in range(len(s)):
            c[s[right]] += 1
            while max(c.values()) > 1:
                c[s[left]] -= 1
                if c[s[left]] == 0:
                    del c[s[left]]
                left += 1
            ans += right - left + 1

        return ans
