class Solution:

    def robotWithString(self, s: str) -> str:

        n = len(s)
        s = list(s)
        t = list()

        suf = [None] * n
        suf[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(suf[i + 1], s[i])

        ans = list()
        for i, c in enumerate(s):
            while t and t[-1] <= suf[i]:
                ans.append(t.pop(-1))
            if c == suf[i]:
                ans.append(c)
            else:
                t.append(c)

        ans += t[::-1]

        return "".join(ans)
