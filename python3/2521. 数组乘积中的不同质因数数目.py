MX = 10 ** 4 + 7
is_prime = [False, False] + [True] * (MX - 2)
for i in range(2, MX - 2):
    if not is_prime[i]:
        continue
    for j in range(i * i, MX - 2, i):
        is_prime[j] = False


class Solution:

    def distinctPrimeFactors(self, nums: List[int]) -> int:

        def f(n):

            if is_prime[n]:
                return {n}

            s = set()
            for i in range(2, n):
                if n % i == 0 and is_prime[i]:
                    s.add(i)

            return s

        s = set()
        for n in nums:
            s |= f(n)

        return len(s)
