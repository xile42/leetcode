MX = 10 ** 5 + 7
is_prime = [False, False] + [True] * (MX - 2)
for i in range(2, MX):
    if not is_prime[i]:
        continue
    for j in range(i * i, MX, i):
        is_prime[j] = False


class Solution:

    def smallestValue(self, n: int) -> int:

        ans = n
        cur = n
        while True:
            next_n = 0
            last_round = cur
            for i in range(2, MX):
                if not is_prime[i]:
                    continue
                while cur % i == 0:
                    next_n += i
                    cur //= i
                if cur == 1:
                    break
            ans = min(ans, next_n)
            if last_round == next_n:
                break
            cur = next_n

        return ans
