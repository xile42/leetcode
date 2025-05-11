class Solution:

    def reinitializePermutation(self, n: int) -> int:

        ns = list(range(n))
        ans = 0
        while True:
            ans += 1
            success = True
            next_ns = [0] * n
            for i in range(n):
                if i & 1:
                    next_ns[i] = ns[n // 2 + (i - 1) // 2]
                else:
                    next_ns[i] = ns[i // 2]
                if next_ns[i] != i:
                    success = False
            if success:
                return ans
            ns = next_ns
