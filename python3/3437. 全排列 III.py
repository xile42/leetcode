class Solution:

    def permute(self, n: int) -> List[List[int]]:

        ans = list()

        def f(ns, cur, is_odd):

            if not ns:
                ans.append(cur)
                return

            for i, v in enumerate(ns):
                if v & 1 == is_odd:
                    f(ns[:i] + ns[i + 1:], cur + [v], 1 - is_odd)

            return

        ns = list(range(1, n + 1))
        f(ns, list(), 1)
        if not n & 1:
            f(ns, list(), 0)

        return sorted(ans)
