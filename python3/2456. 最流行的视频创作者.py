class Solution:

    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:

        c = Counter()
        d = defaultdict(lambda: (-inf, ""))
        for author, _id, view in zip(creators, ids, views):
            c[author] += view
            if view > d[author][0] or (view == d[author][0] and _id < d[author][1]):
                d[author] = (view, _id)

        mx = max(c.values())
        ans = list()
        for author in c:
            if c[author] == mx:
                ans.append([author, d[author][1]])

        return ans
