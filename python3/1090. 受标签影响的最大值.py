class Solution:

    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:

        n = len(values)
        ns = sorted([[v, l] for v, l in zip(values, labels)], reverse=True, key=lambda x: x[0])
        ans = i = 0
        c = Counter()
        cnt = 0
        while cnt < numWanted and i < n:
            v, l = ns[i]
            if c[l] < useLimit:
                ans += v
                c[l] += 1
                cnt += 1
            i += 1

        return ans
