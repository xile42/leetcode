"""
codeforces-python: 算法竞赛Python3模板库
#3: KMP算法
https://github.com/xile42/codeforces-python/blob/main/templates/string.py
"""
class KMP:

    def __init__(self, pattern: str):

        self.pattern = pattern
        self.n = len(self.pattern)
        self.pi = self._run()

    def _run(self) -> List[int]:
        """ 计算前缀函数 """

        pi = [0] * self.n
        match = 0
        for i in range(1, self.n):
            while match > 0 and self.pattern[i] != self.pattern[match]:
                match = pi[match - 1]
            if self.pattern[i] == self.pattern[match]:
                match += 1
            pi[i] = match

        return pi

    def search(self, text: str) -> List[int]:
        """ 在文本中搜索模式串 """

        pos = list()
        match = 0
        for i in range(len(text)):
            while match > 0 and text[i] != self.pattern[match]:
                match = self.pi[match - 1]
            if text[i] == self.pattern[match]:
                match += 1
            if match == len(self.pattern):
                pos.append(i - len(self.pattern) + 1)
                match = self.pi[match - 1]

        return pos

    def has_repeated_substring(self) -> bool:
        """ 检测模式串是否由某个子串重复多次构成 """

        if self.n == 0:
            return False
        # 检查是否满足 n % (n - π[n-1]) == 0 且 π[n-1] != 0
        return self.pi[-1] != 0 and self.n % (self.n - self.pi[-1]) == 0

    def get_repeated_substring(self) -> Optional[str]:
        """ 获取构成模式串的循环节(如果存在) """

        if self.n == 0 or self.pi[-1] == 0:
            return None

        if self.n % (self.n - self.pi[-1]) == 0:
            return self.pattern[:self.n - self.pi[-1]]

        return None


class Solution:

    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:

        n = len(nums)
        s = "".join(["a" if nums[i] > nums[i - 1] else ("b" if nums[i] == nums[i - 1] else "c") for i in range(1, n)])
        d = {1: "a", 0: "b", -1: "c"}
        pattern = "".join([d[v] for v in pattern])

        kmp = KMP(pattern)
        pos = kmp.search(s)

        return len(pos)
