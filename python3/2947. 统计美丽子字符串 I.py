class Solution:

    def beautifulSubstrings(self, s: str, k: int) -> int:

        valid = {"a", "e", "i", "o", "u"}
        n = len(s)
        ans = 0
        for i in range(n):
            a = b = 0
            for j in range(i, n):
                if s[j] in valid:
                    a += 1
                else:
                    b += 1
                if a == b and (a * b) % k == 0:
                    ans += 1

        return ans
