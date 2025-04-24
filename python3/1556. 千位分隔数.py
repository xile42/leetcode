class Solution:

    def thousandSeparator(self, n: int) -> str:

        s = str(n)[::-1]
        result = list()
        idx = 0
        while idx < len(s):
            result.append(s[idx:idx+3])
            idx += 3

        return ".".join(result)[::-1]
