from itertools import pairwise

MX = 10 ** 6 + 7
is_prime = [False, False] + [True] * (MX - 2)
for i in range(2, MX - 2):
    if not is_prime[i]:
        continue
    for j in range(i * i, MX - 2, i):
        is_prime[j] = False


class Solution:

    def closestPrimes(self, left: int, right: int) -> List[int]:

        ns = list()
        for n in range(left, right + 1):
            if is_prime[n]:
                ns.append(n)

        ans = [-1, -1]
        cur = inf
        for a, b in pairwise(ns):
            if b - a < cur:
                cur = b - a
                ans = [a, b]

        return ans
