class Solution:

    def diagonalPrime(self, nums: List[List[int]]) -> int:

        def is_prime(n):

            if n == 1:
                return False

            for i in range(2, n):
                if n % i == 0:
                    return False

            return True

        n = len(nums)
        ns = set()
        for i in range(n):
            ns.add(nums[i][i])
            ns.add(nums[i][n - 1 - i])

        ns = sorted(ns, reverse=True)
        for v in ns:
            if is_prime(v):
                return v

        return 0
