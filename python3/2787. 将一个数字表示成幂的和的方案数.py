class Solution:

    def numberOfWays(self, n: int, x: int) -> int:

        base = 10 ** 9 + 7
        choices = list()
        for i in range(1, n + 1):
            v = pow(i, x)
            if v <= n:
                choices.append(v)
            else:
                break

        @cache
        def f(cur, tar):

            if tar < 0:
                return None

            if tar == 0:
                return 1

            if cur >= len(choices):
                return None

            ans = 0
            cur_val = choices[cur]
            for i in range(2):
                res = f(cur + 1, tar - i * cur_val)
                if res is not None:
                    ans += res % base
                    ans %= base

            return ans

        ans = f(0, n)
        f.cache_clear()

        return ans
