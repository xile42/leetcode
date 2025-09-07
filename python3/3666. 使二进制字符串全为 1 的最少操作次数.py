class Solution:

    def minOperations(self, s: str, k: int) -> int:

        n = len(s)
        m = sum(1 for char in s if char == "0")

        if m == 0:
            return 0

        if k == n:
            if m == n:
                return 1
            else:
                return -1

        if not k & 1 and m & 1:
            return -1

        v = (m + k - 1) // k

        if not k & 1:
            t = v
            while True:
                if not t & 1:
                    if m <= t * (n - k):
                        return t
                else:
                    if t * k <= n * (t - 1) + m:
                        return t
                t += 1
        else:
            if v & 1 == m & 1:
                t = v
            else:
                t = v + 1
            while True:
                if not t & 1:
                    if m <= t * (n - k):
                        return t
                else:
                    if t * k <= n * (t - 1) + m:
                        return t
                t += 2
