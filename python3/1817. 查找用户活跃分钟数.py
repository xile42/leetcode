class Solution:

    def findingUsersActiveMinutes(self, logs: List[List[int]], tar: int) -> List[int]:

        d = defaultdict(set)
        for i, t in logs:
            d[i].add(t)

        dd = defaultdict(list)
        for k, v in d.items():
            dd[len(v)].append(k)

        ans = list()
        for i in range(tar):
            ans.append(len(dd[i + 1]))

        return ans
