class Solution:

    def minFlipsMonoIncr(self, s: str) -> int:

        n = len(s)

        @cache
        def f(i, is_limit):

            if i >= n:
                return 0

            ans = inf
            cur = s[i]
            if is_limit:
                if cur == "0":
                    ans = min(ans, 1 + f(i + 1, True))
                else:
                    ans = min(ans, f(i + 1, True))
            else:
                if cur == "0":
                    ans = min(ans, 1 + f(i + 1, True))
                    ans = min(ans, f(i + 1, False))
                else:
                    ans = min(ans, 1 + f(i + 1, False))
                    ans = min(ans, f(i + 1, True))

            return ans

        return f(0, False)
