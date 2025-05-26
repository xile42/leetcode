class Solution:

    def minSwaps(self, s: str) -> int:
        cnt = 0
        mx = 0
        for i in range(len(s)):
            cnt += -1 if s[i] == "]" else 1
            mx = max(mx, -cnt)

        return ceil(mx / 2)
