class Solution:

    def mostPoints(self, questions: List[List[int]]) -> int:

        n = len(questions)

        @cache
        def f(i):

            if i >= n:
                return 0

            ans = 0
            ans = max(ans, questions[i][0] + f(i + questions[i][1] + 1), f(i + 1))

            return ans

        return f(0)
