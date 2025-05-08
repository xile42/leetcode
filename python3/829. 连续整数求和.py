def f(n):
    ans = list()
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            ans.append([i, n // i])

    return ans


class Solution:

    def consecutiveNumbersSum(self, n: int) -> int:

        s = set()

        # [n]
        s.add((n, 1))

        if n & 1:
            # [(n - 1) // 2, (n + 1) // 2]
            s.add(((n - 1) // 2, 2))

        # length >= 3
        factor_pairs = f(n)

        for a, b in factor_pairs:
            if a == b:
                if a & 1:
                    s.add((a - ((a - 1) // 2), a))
                continue
            if not a & 1 and not b & 1:
                pass
            elif a & 1 and not b & 1:
                if a == b - 1:
                    s.add(((a - 1) // 2 - (b - 1), b * 2))
                s.add((b - ((a - 1) // 2), a))
            elif not a & 1 and b & 1:
                s.add((a - ((b - 1) // 2), b))
                s.add(((b - 1) // 2 - (a - 1), a * 2))
            else:
                if b <= 2 * a + 1:
                    s.add(((a - 1) // 2 - ((b - 1) // 2), b * 2))
                s.add(((b - 1) // 2 - (a // 2), a * 2))
                s.add((b - ((a - 1) // 2), a))


        for a, b in list(s):
            if a == 0:
                s.remove((a, b))
                s.add((a + 1, b - 1))
            if a < 0:
                s.remove((a, b))

        return len(s)
