class Solution:

    def summaryRanges(self, nums: List[int]) -> List[str]:

        ns = [[n, n - i] for i, n in enumerate(nums)]
        d = defaultdict(list)
        for n, k in ns:
            d[k].append(n)

        ans = list()
        for k in sorted(d.keys()):
            v = d[k]
            if len(v) == 1:
                ans.append(str(v[0]))
            else:
                ans.append("{}->{}".format(v[0], v[-1]))

        return ans
