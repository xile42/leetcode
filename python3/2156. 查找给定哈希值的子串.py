"""
codeforces-python: 算法竞赛Python3模板库
#1: 单模-字符串哈希
https://github.com/xile42/codeforces-python/blob/main/templates/string.py
"""
class StringHashSingleMod:

    def __init__(self, s: str, mod, base):

        self.s = s
        self.n = len(s)
        # mod 与 base 随机一个即可, 以避免被hack
        self.mod = mod
        self.base = base
        self.pow_base = [1] * (self.n + 1)
        self.pre_hash = [0] * (self.n + 1)
        self._run()

    def _run(self):
        """ 预处理哈希值, 多项式系数前缀和数组 """

        for i in range(1, self.n + 1):
            self.pow_base[i] = (self.pow_base[i - 1] * self.base) % self.mod
            self.pre_hash[i] = (self.pre_hash[i - 1] * self.base + ord(self.s[i - 1]) - ord("a") + 1) % self.mod

    def get_hash(self, l: int, r: int) -> int:
        """ 获取子串哈希值 [l, r] """

        return ((self.pre_hash[r + 1] - self.pre_hash[l] * self.pow_base[r + 1 - l]) % self.mod + self.mod) % self.mod


class Solution:

    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:

        s = s[::-1]
        s_hash = StringHashSingleMod(s, modulo, power)
        n = len(s)

        for i in range(n - k, -1, -1):
            cur = s_hash.get_hash(i, i + k - 1)
            if cur == hashValue:
                return s[i:i + k][::-1]
