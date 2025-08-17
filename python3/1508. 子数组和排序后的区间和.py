class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        acc = list(accumulate(nums))

        def f(i, j):

            return acc[j] - (acc[i - 1] if i > 0 else 0)

        ns = list()
        for i in range(n):
            for j in range(i, n):
                ns.append(f(i, j))
        ns.sort()

        ans = 0
        base = 10 ** 9 + 7
        for i in range(left - 1, right):
            ans += ns[i] % base
            ans %= base

        return ans
