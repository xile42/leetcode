class Solution:

    def getHappyString(self, n: int, k: int) -> str:

        ans = list()

        def f(cur, left):

            nonlocal ans
            if len(ans) >= k:
                return
            if left == 0:
                ans.append(cur)
                return

            c = cur[-1]
            for cc in ["a", "b", "c"]:
                if cc != c:
                    f(cur + cc, left - 1)


        for c in ["a", "b", "c"]:
            f(c, n - 1)

        return str() if len(ans) < k else ans[k - 1]
