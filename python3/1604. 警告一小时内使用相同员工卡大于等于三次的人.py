class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        c = defaultdict(list)
        for n, t in zip(keyName, keyTime):
            h, m = map(int, t.split(":"))
            t = h * 60 + m
            c[n].append(t)

        ans = set()
        for n, ts in c.items():
            ts.sort()
            for i in range(2, len(ts)):
                if ts[i] - ts[i - 2] <= 60:
                    ans.add(n)
                    break

        return sorted(ans)
