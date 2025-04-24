# from functools import cache
#
#
# class Solution:
#
#     base = pow(10, 9) + 7
#
#     @cache
#     def f(self, i, t):
#
#         if t < 26 - i:
#             return 0
#
#         if t == 0:
#             return 0
#
#         return (1 + self.f(0, t - (26 - i)) + self.f(1, t - (26 - i))) % self.base
#
#     def lengthAfterTransformations(self, s: str, t: int) -> int:
#
#         result = len(s)
#         for char in s:
#             i = ord(char) - ord("a")
#             result += self.f(i, t) % self.base
#
#         return result
#
#
# foo = Solution()
# print(len("jqktcurgdvlibczdsvnsg"))
# print(foo.lengthAfterTransformations("jqktcurgdvlibczdsvnsg", 1))


class Solution:

    def lengthAfterTransformations(self, s: str, t: int) -> int:

        results = 0
        base = pow(10, 9) + 7
        f = [0] * (t + 26)
        for i in range(26):
            f[i] = 1
        for i in range(26, t + 26):
            f[i] = (f[i - 26] + f[i - 26 + 1]) % base

        for char in s:
            i = ord(char) - ord("a")
            results += f[t + i] % base

        return results % base