class Solution:

    def solveEquation(self, equation: str) -> str:

        left, right = equation.split("=")

        def parse(s):

            a, b = 0, 0
            xs = re.findall("[+-]*\d*x", s)
            nums = re.findall("[+-]*\d+(?=[+-]|$)", s)

            for i in xs:
                t = i[:-1]
                a += int(t+"1") if t in ["+", "-", ""] else int(t)

            for i in nums:
                if i[-1] in ["+", "-"]:
                    b += int(i[:-1])
                else:
                    b += int(i)

            return a, b

        a, b = parse(left)
        c, d = parse(right)

        x = a - c
        d = d - b

        if x == 0:
            return "Infinite solutions" if d == 0 else "No solution"

        if abs(d) % abs(x) != 0:
            return "No solution"

        ans = d // x
        return "x={}".format(ans)
