class Solution:

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        ans = list()
        d = defaultdict(lambda: -1)
        c = Counter()

        for i, j in queries:

            old = d[i]
            c[old] -= 1
            if c[old] == 0:
                del c[old]

            d[i] = j
            c[j] += 1

            ans.append(len(c))
            ans[-1] -= 1 if -1 in c else 0

        return ans
