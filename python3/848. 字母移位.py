"""
codeforces-python: 算法竞赛Python3模板库
#1: 一维差分(数组实现)
https://github.com/xile42/codeforces-python/blob/main/templates/diff_array.py
"""
class DiffArray:

    @staticmethod
    def diff_accumulate(n: int, lrws: List[Tuple[int, int, int]]) -> List[int]:

        diff = [0] * (n + 1)  # 默认下标从0开始(对应l, r)

        for l, r, w in lrws:
            diff[l] += w
            diff[r + 1] -= w

        ans = list()
        cur = 0
        for i in range(n):
            cur += diff[i]
            ans.append(cur)

        return ans  # 默认返回长度n


class Solution:

    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        diff = DiffArray.diff_accumulate(len(s), [(0, i, shifts[i]) for i in range(len(shifts))])
        ans = list()
        for c, d in zip(s, diff):
            ans.append(chr((ord(c) - ord('a') + d) % 26 + ord('a')))

        return "".join(ans)
