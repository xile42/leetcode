class Solution:

    def countPalindromicSubsequence(self, s: str) -> int:

        pre = [set()] * len(s)
        pre[0] = {s[0]}
        for i in range(1, len(s)):
            t = pre[i - 1].copy()
            t.add(s[i])
            pre[i] = t

        suf = [set()] * len(s)
        suf[-1] = {s[-1]}
        for i in range(len(s) - 2, -1, -1):
            t = suf[i + 1].copy()
            t.add(s[i])
            suf[i] = t

        h = set()
        ans = 0
        for i in range(1, len(s) - 1):
            c = s[i]
            for cc in pre[i - 1] & suf[i + 1]:
                this = cc + c + cc
                if this not in h:
                    ans += 1
                    h.add(this)

        return ans
