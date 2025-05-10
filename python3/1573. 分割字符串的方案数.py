class Factorial:

    def __init__(self, N, mod) -> None:
        N += 1
        self.mod = mod
        self.f = [1 for _ in range(N)]
        self.g = [1 for _ in range(N)]
        for i in range(1, N):
            self.f[i] = self.f[i - 1] * i % self.mod
        self.g[-1] = pow(self.f[-1], mod - 2, mod)
        for i in range(N - 2, -1, -1):
            self.g[i] = self.g[i + 1] * (i + 1) % self.mod

    def fac(self, n):
        return self.f[n]

    def fac_inv(self, n):
        return self.g[n]

    def combi(self, n, m):
        if n < m or m < 0 or n < 0: return 0
        return self.f[n] * self.g[m] % self.mod * self.g[n - m] % self.mod

    def permu(self, n, m):
        if n < m or m < 0 or n < 0: return 0
        return self.f[n] * self.g[n - m] % self.mod

    def catalan(self, n):
        return (self.combi(2 * n, n) - self.combi(2 * n, n - 1)) % self.mod

    def inv(self, n):
        return self.f[n-1] * self.g[n] % self.mod


mod = 10 ** 9 + 7
f = Factorial(10 ** 5 + 1000, mod)


class Solution:

    def numWays(self, s: str) -> int:

        n = len(s)
        cnt = s.count("1")
        if cnt % 3 != 0:
            return 0

        if cnt == 0:
            return f.combi(n - 1, 2)

        k1, k2 = cnt // 3, cnt // 3 * 2
        s1 = e1 = s2 = e2 = None
        cnt = 0
        for i, c in enumerate(s):
            if c == "1":
                cnt += 1
                if cnt == k1:
                    s1 = i
                if cnt == k1 + 1:
                    e1 = i
                if cnt == k2:
                    s2 = i
                if cnt == k2 + 1:
                    e2 = i

        return (f.combi(e1 - s1, 1) * f.combi(e2 - s2, 1)) % mod
