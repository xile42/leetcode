class Solution:

    def uniqueLetterString(self, s: str) -> int:

        base = ord("A")
        n = len(s)
        pre = [[None] * 26 for _ in range(n)]
        suf = [[None] * 26 for _ in range(n)]

        cur = [None] * 26
        for i, c in enumerate(s):
            for j in range(26):
                pre[i][j] = cur[j]
            cur[ord(c) - base] = i

        cur = [None] * 26
        for i in range(n - 1, -1, -1):
            c = s[i]
            for j in range(26):
                suf[i][j] = cur[j]
            cur[ord(c) - base] = i

        ans = 0
        for i, c in enumerate(s):
            left_idx = pre[i][ord(c) - base]
            right_idx = suf[i][ord(c) - base]
            left = i + 1 if left_idx is None else i - left_idx
            right = n - i if right_idx is None else right_idx - i
            ans += left * right

        return ans
