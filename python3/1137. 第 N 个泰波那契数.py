class Solution:

    def tribonacci(self, n: int) -> int:

        f = [0, 1, 1]
        if n <= 2:
            return f[n]

        for _ in range(n - 2):
            f.append(f[-3] + f[-2] + f[-1])

        return f[-1]
