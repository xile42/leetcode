class Solution:

    def countSubstrings(self, s: str, t: str) -> int:

        subs = list()
        for i in range(len(s)):
            cur = str()
            for j in range(i, len(s)):
                cur += s[j]
                subs.append(cur)

        subt = list()
        for i in range(len(t)):
            cur = str()
            for j in range(i, len(t)):
                cur += t[j]
                subt.append(cur)

        cs = Counter(subs)
        ct = Counter(subt)
        ans = 0
        for _s, cnt in ct.items():
            for i in range(len(_s)):
                c = _s[i]
                for cc in string.ascii_lowercase:
                    if c == cc:
                        continue
                    tar_s = _s[:i] + cc + _s[i + 1:]
                    ans += cs[tar_s] * cnt

        return ans
