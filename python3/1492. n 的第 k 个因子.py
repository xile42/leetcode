class Solution:

    def kthFactor(self, n: int, k: int) -> int:

        factors = list()
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
            if len(factors) == k:
                break

        return -1 if len(factors) < k else factors[-1]
