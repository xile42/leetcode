class Solution:

    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        d = defaultdict(list)
        for i, s in items:
            d[i].append(s)

        ans = list()
        for k in sorted(d.keys()):
            ans.append([k, sum(sorted(d[k])[-5:]) // 5])

        return ans
