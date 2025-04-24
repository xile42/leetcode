class Solution:

    def generateTheString(self, n: int) -> str:

        cs = string.ascii_lowercase

        def f(n, cur):

            if n & 1:
                return cs[cur] * n
            else:
                return cs[cur] * (n - 1) + cs[cur+1] * 1

        return f(n, 0)
