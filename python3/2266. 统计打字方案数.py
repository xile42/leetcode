MOD = 1_000_000_007
f = [1, 1, 2, 4]
g = [1, 1, 2, 4]
for _ in range(10 ** 5 - 3):  # 预处理所有长度的结果
    f.append((f[-1] + f[-2] + f[-3]) % MOD)
    g.append((g[-1] + g[-2] + g[-3] + g[-4]) % MOD)


class Solution:

    def countTexts(self, pressedKeys: str) -> int:

##        base = pow(10, 9) + 7
##
##        @cache
##        def f(n):
##
##            if n == 0:
##                return 1
##
##            result = 0
##            for i in range(1, 4):
##                if n - i >= 0:
##                    result += f(n-i)
##
##            return result
##
##        @cache
##        def g(n):
##
##            if n == 0:
##                return 1
##
##            result = 0
##            for i in range(1, 5):
##                if n - i >= 0:
##                    result += g(n-i)
##
##            return result

        result = 1
        for char, ite in groupby(pressedKeys):
            cnt = len(list(ite))
            v = f[cnt] if char not in "79" else g[cnt]
            result *= v
            result %= MOD

        return result
