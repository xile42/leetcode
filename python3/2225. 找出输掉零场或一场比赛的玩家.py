class Solution:

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        s = set()
        c = Counter()
        for w, l in matches:
            s.add(w)
            s.add(l)
            c[l] += 1

        ans = [[], []]
        for p in s:
            if c[p] == 0:
                ans[0].append(p)
            elif c[p] == 1:
                ans[1].append(p)

        return [sorted(ans[0]), sorted(ans[1])]
