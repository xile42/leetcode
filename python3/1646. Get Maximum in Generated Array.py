class Solution:

    @cache
    def f(self, num):

        if num <= 0:
            return 0
        if num == 1:
            return 1

        if num & 1:
            return self.f(num // 2) + self.f(num // 2 + 1)
        else:
            return self.f(num // 2)

    def getMaximumGenerated(self, n: int) -> int:

        return max([self.f(i) for i in range(n+1)])
