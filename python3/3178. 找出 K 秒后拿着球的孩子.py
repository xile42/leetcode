class Solution:

    def numberOfChild(self, n: int, k: int) -> int:

        t, r = divmod(k, n - 1)
        if t & 1:
            return n - 1 - r
        else:
            return r
