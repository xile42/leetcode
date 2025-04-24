class Solution:

    def maxScore(self, s: str) -> int:

        n = len(s)
        f, g = [0] * (n+1), [0] * (n+1)
        for idx, char in enumerate(s):
            if char == "0":
                f[idx+1] = f[idx] + 1
            else:
                f[idx+1] = f[idx]
        for idx, char in enumerate(s[::-1]):
            if char == "1":
                g[idx+1] = g[idx] + 1
            else:
                g[idx+1] = g[idx]

        result = -1
        for left_length in range(1, n):
            right_length = n - left_length
            result = max(result, f[left_length]+g[right_length])

        return result
