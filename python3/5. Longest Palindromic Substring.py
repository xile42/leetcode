class Solution:

    def longestPalindrome(self, s: str) -> str:

        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]

        for idx in range(length):
            dp[idx][idx] = 1
        for idx in range(length-1):
            if s[idx] == s[idx+1]:
                dp[idx][idx+1] = 1

        for step in range(2, length):
            for idx in range(length):
                jdx = idx + step
                if not jdx < length:
                    break
                dp[idx][jdx] = 1 if dp[idx+1][jdx-1] == 1 and s[idx] == s[jdx] else 0

        max_length = 0
        result = None
        for idx in range(length):
            for jdx in range(idx, length):
                if dp[idx][jdx] == 1 and jdx - idx + 1 > max_length:
                    max_length = jdx-idx+1
                    result = [idx, jdx]

        return s[result[0]:result[1]+1]
