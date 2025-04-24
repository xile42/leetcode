class Solution:

    def totalNQueens(self, n: int) -> int:

        ans = 0

        def check(i, j, cur):

            for x, y in cur:
                if j == y or abs(y - j) == abs(x - i):
                    return False

            return True

        def f(cur):

            nonlocal ans
            if len(cur) == n:
                ans += 1

            i = len(cur)
            for j in range(n):
                if check(i, j, cur):
                    f(cur + [[i, j]])

        f([])

        return ans
