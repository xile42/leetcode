class Solution:

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        cs = [Counter(s) for s in words]
        ks = [min(c.keys()) for c in cs]
        ns = list([cs[i][ks[i]] for i in range(len(cs))])
        ns.sort()

        ans = list()
        for s in queries:
            c = Counter(s)
            v = c[min(c.keys())]
            ans.append(len(ns) - bisect_right(ns, v))

        return ans