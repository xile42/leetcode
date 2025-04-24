class Solution:

    def pivotInteger(self, n: int) -> int:

        acc = [0] + list(accumulate(range(1, n + 1)))
        for i in range(n // 2, n):
            l = acc[i + 1] - acc[0]
            r = acc[-1] - acc[i]
            if l == r:
                return i + 1
            elif l > r:
                return -1

        return -1
