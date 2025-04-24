class Solution:

    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        def parse(s):

            a, others = s.split("+")
            b = others[:-1]

            return int(a), int(b)

        a, b = parse(num1)
        c, d = parse(num2)

        r1 = a * c - b * d
        r2 = b * c + a * d

        return "{}+{}i".format(r1, r2)
