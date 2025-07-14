min = lambda a, b: a if a < b else b
max = lambda a, b: a if a > b else b


"""
codeforces-python: 算法竞赛Python3模板库
#2: 回文字符串生成器(记忆化搜索)
https://github.com/xile42/codeforces-python/blob/main/templates/common.py
"""
class PalindromeStringGenerator:

    def __init__(self, s: str) -> None:

        self.s = s
        self.palindromes = set()
        self._init_palindromes()

    def _init_palindromes(self) -> None:

        n = len(self.s)
        for mask in range(1, 1 << n):  # 跳过空子集(mask = 0)
            subset = [self.s[i] for i in range(n) if mask & (1 << i)]
            self._process_subset(subset)

        self.palindromes = sorted(self.palindromes, key=lambda x: len(x), reverse=True)

    def _process_subset(self, subset: List[str]) -> None:

        counter = Counter(subset)
        odd_chars = [char for char, freq in counter.items() if freq % 2 == 1]

        if len(odd_chars) > 1:  # 无法形成回文
            return

        middle = odd_chars[0] if odd_chars else ""
        left_chars = list()
        for char, freq in counter.items():
            left_chars.extend([char] * (freq // 2))

        # 生成左半部分的全排列
        for perm in set(permutations(left_chars)):
            left = "".join(perm)
            self.palindromes.add(left + middle + left[::-1])


class Solution:

    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:

        valids = PalindromeStringGenerator(label).palindromes
        ans = 1
        d = defaultdict(list)
        for i, c in enumerate(label):
            d[c].append(i)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(i, tar_idx):

            if tar_idx >= len(tar):
                return True

            vis.add(i)
            for j in g[i]:
                if j in vis or label[j] != tar[tar_idx]:
                    continue
                check = dfs(j, tar_idx + 1)
                if check:
                    return True

            return False

        for tar in valids:
            for start in d[tar[0]]:
                vis = set()
                check = dfs(start, 1)
                if check:
                    ans = max(ans, len(tar))
                    return ans

        return ans
