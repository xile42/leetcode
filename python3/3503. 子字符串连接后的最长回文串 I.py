class Solution:

    def longestPalindrome(self, s: str, t: str) -> int:

        parts_s = [""]
        parts_t = [""]
        for l in range(1, len(s) + 1):
            for i in range(len(s)):
                parts = s[i:i + l]
                if len(parts) != l:
                    break
                parts_s.append(parts)
        for l in range(1, len(t) + 1):
            for i in range(len(t)):
                parts = t[i:i + l]
                if len(parts) != l:
                    break
                parts_t.append(parts)

        @cache
        def is_hw(s):

            if len(s) <= 1:
                return True

            if s[0] == s[-1]:
                return is_hw(s[1:-1])
            else:
                return False

        ans = 0
        for s1 in parts_s:
            for s2 in parts_t:
                if len(s1) + len(s2) <= ans:
                    continue
                if is_hw(s1 + s2):
                    ans = max(ans, len(s1) + len(s2))

        is_hw.cache_clear()

        return ans
