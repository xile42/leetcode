class Solution:

    def commonChars(self, words: List[str]) -> List[str]:

        results = list()
        cs = [Counter(i) for i in words]
        ks = [set(i.keys()) for i in cs]
        if len(ks) == 0:
            return results
        valid = ks[0]
        for k in ks[1:]:
            valid &= k
        for k in valid:
            v = min(c[k] for c in cs)
            results += list(k * v)

        return results
        
