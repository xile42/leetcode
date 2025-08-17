class Solution:

    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:

        all_ws = list()
        head = defaultdict(list)
        for i, s in enumerate(phrases):
            ws = s.split()
            head[ws[0]].append((ws, i))
            all_ws.append((ws, i))

        ans = set()
        for ws, i in all_ws:
            tar = ws[-1]
            for other_ws, j in head[tar]:
                if i != j:
                    ans.add(" ".join(ws + other_ws[1:]))

        return sorted(ans)
