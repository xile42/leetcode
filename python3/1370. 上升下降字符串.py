class Solution:

    def sortString(self, s: str) -> str:

        order = string.ascii_lowercase
        c = Counter(s)
        result = str()

        while len(result) < len(s):

            for k in order:
                v = c[k]
                if v > 0:
                    result += k
                    c[k] -= 1

            for k in order[::-1]:
                v = c[k]
                if v > 0:
                    result += k
                    c[k] -= 1

        return result
