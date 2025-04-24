class Solution:

    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        c = Counter(digits)
        digits = reduce(add, [[k] * min(v, 3) for k, v in c.items()])
        s = set()
        for i in permutations(digits, 3):
            t = int("".join(map(str, i)))
            if t >= 100 and not t & 1:
                s.add(t)

        return sorted(s)

##        ans = list()
##
##        def f(ns, cur):
##
##            nonlocal ans
##            if len(cur) == 3:
##                ans.append(int(cur))
##
##            vis = [False] * 10
##            for i, n in enumerate(ns):
##                if vis[n]:
##                    continue
##                if len(cur) == 0 and n == 0:
##                    continue
##                if len(cur) == 2 and n & 1:
##                    continue
##                f(ns[:i]+ns[i+1:], cur+str(n))
##                vis[n] = True
##
##        f(digits, str())
##
##        return sorted(set(ans))
