k = 5 * 10 ** 6
ns = [1] * (k + 1)
ns[0] = ns[1] = 0
for i in range(2, k + 1):
    if not ns[i]:
        continue
    cur = i * i
    while cur <= k:
        ns[cur] = 0
        cur += i
acc = list(accumulate(ns))

class Solution:

    def countPrimes(self, n: int) -> int:

        if n <= 1:
            return 0

        return acc[n - 1]
