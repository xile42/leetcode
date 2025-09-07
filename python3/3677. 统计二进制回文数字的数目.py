class Solution:

    def countBinaryPalindromes(self, n: int) -> int:

        if n == 0:
            return 1
        if n == 1:
            return 2

        s = bin(n)[2:]
        length = len(s)
        ans = 1

        if length > 1:
            M = length - 2
            if M > 0:
                if not M & 1:
                    k = M // 2
                    S = 3 * ((1 << k) - 1)
                else:
                    k = (M - 1) // 2
                    S = (1 << (k + 2)) - 3
                ans += 1 + S
            else:
                ans += 1

        half = (length + 1) // 2
        ss = s[:half]
        start = 1 << (half - 1)
        ss_val = int(ss, 2)
        ans1 = ss_val - start

        if not length & 1:
            pal = ss + ss[::-1]
        else:
            pal = ss + ss[:-1][::-1]
        v = int(pal, 2)
        ans2 = 1 if v <= n else 0

        ans += ans1 + ans2

        return ans
