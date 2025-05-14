MX = 10 ** 6 + 1
is_prime = [True] * (MX + 1)
primes = list()
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MX, i):
            is_prime[j] = False


class Solution:

    def findPrimePairs(self, n: int) -> List[List[int]]:

        ans = list()
        for x in primes:
            if x > n - x:
                break
            if is_prime[n - x]:
                ans.append([x, n - x])

        return ans
