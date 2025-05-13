class Solution:

    def makePalindrome(self, s: str) -> bool:

        n = len(s)
        cnt = 0
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                cnt += 1

        return cnt <= 2
