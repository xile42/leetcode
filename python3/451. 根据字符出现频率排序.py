class Solution:

    def frequencySort(self, s: str) -> str:

        c = Counter(s)
        kvs = sorted([[v, k] for k, v in c.items()], key=lambda x: x[0], reverse=True)
        ans = list()
        for v, k in kvs:
            ans += [k] * v

        return "".join(ans)
