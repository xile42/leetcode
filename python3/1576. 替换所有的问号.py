class Solution:

    def modifyString(self, s: str) -> str:

        vs = string.ascii_lowercase
        result = list(s)
        for i, c in enumerate(s):
            if c.isalpha():
                result[i] = c
            else:
                left = None if i - 1 < 0 else result[i - 1]
                right = None if i + 1 >= len(s) else result[i + 1]
                for cc in vs:
                    if cc != left and cc != right:
                        result[i] = cc
                        break

        return "".join(result)
