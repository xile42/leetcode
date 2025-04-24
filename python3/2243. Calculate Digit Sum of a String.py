class Solution:

    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            parts = list()
            while s:
                parts.append(str(sum(map(int, s[:k]))))
                s = s[k:]
            s = "".join(parts)

        return s
