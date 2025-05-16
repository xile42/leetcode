class Solution:

    def generateParenthesis(self, n: int) -> List[str]:

        if n == 0:
            return list()

        ans = list()

        def f(cur, left):

            nonlocal ans
            if len(cur) == 2 * n:
                ans.append(cur)
                return

            if left < n:
                f(cur + "(", left + 1)
            if len(cur) - left < left:
                f(cur + ")", left)

        f("", 0)

        return ans
