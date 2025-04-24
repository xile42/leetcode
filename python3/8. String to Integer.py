class Solution:

    boundary = pow(2, 31)

    def myAtoi(self, s: str) -> int:

        while len(s) and s[0] == " ":
            s = s[1:]

        sign = 1
        if len(s):
            sign = -1 if s[0] == "-" else 1
            if s[0] in ["+", "-"]:
                s = s[1:]

        while len(s) and s[0] == "0":
            s = s[1:]

        result = str()
        while len(s) and s[0] in "0123456789":
            result += s[0]
            s = s[1:]

        result = 0 if len(result) == 0 else int(result) * sign
        if result < 0 and result < -self.boundary:
            result = -self.boundary
        elif result > 0 and result > self.boundary - 1:
            result = self.boundary - 1

        return result

