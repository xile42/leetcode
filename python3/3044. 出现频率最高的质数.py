from math import isqrt


class Solution:

    def mostFrequentPrime(self, mat: List[List[int]]) -> int:

        m, n = len(mat), len(mat[0])
        offsets = [
            [0, 1],
            [1, 1],
            [1, 0],
            [1, -1],
            [0, -1],
            [-1, -1],
            [-1, 0],
            [-1, 1],
        ]

        def f(i, j):

            ans = list()
            for oi, oj in offsets:
                paths = list()
                cur = str(mat[i][j])
                ii, jj = i, j
                while 0 <= (ii := ii + oi) < m and 0 <= (jj := jj + oj) < n:
                    cur += str(mat[ii][jj])
                    paths.append(int(cur))
                ans += paths

            return ans

        def is_prime(x):
            for i in range(2, isqrt(x) + 1):
                if x % i == 0:
                    return False
            return x > 1

        vs = list()
        for i in range(m):
            for j in range(n):
                vs += f(i, j)

        c = Counter(vs)
        kvs = sorted([[v, k] for k, v in c.items()], reverse=True)
        ans = list()
        maxf = -inf
        for v, k in kvs:
            if v < maxf:
                break
            if is_prime(k):
                ans.append(k)
                maxf = max(maxf, v)

        return -1 if not ans else max(ans)
