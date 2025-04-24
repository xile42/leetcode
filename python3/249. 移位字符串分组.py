class Solution:

    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        d = defaultdict(list)
        for s in strings:
            k = [(ord(s[i]) - ord(s[i - 1]) + 26) % 26 for i in range(1, len(s))]
            d[tuple(k)].append(s)

        return list(d.values())
