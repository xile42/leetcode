class Solution:

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        ans = set()

        def f(cur, left):

            nonlocal ans
            if left == 0:
                ans.add(int(cur))
                return

            c, ic = cur[-1], int(cur[-1])
            if ic + k < 10:
                f(cur + str(ic + k), left - 1)
            if ic - k >= 0:
                f(cur + str(ic - k), left - 1)

        for i in range(1, 10):
            f(str(i), n - 1)

        return list(ans)
