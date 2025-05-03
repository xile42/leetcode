class Solution:

    def getFactors(self, n: int) -> List[List[int]]:

        @cache
        def f(x, start):

            if x == 1:
                return [[]]

            ans = list()
            for i in range(start, isqrt(x) + 1):
                if x % i == 0:
                    ans.append([i, x // i])
                    ans += [[i] + sub_ans for sub_ans in f(x // i, i)]

            return ans

        ans = f(n, 2)
        ans = [i for i in ans if len(i) > 1]

        return ans
