class Solution:

    def convertDateToBinary(self, date: str) -> str:

        y, m, d = list(map(int, date.split("-")))
        y, m, d = bin(y)[2:], bin(m)[2:], bin(d)[2:]

        while len(y) and y[0] == "0":
            y = y[1:]
        if len(y) == 0:
            y = "0"

        while len(m) and m[0] == "0":
            m = m[1:]
        if len(m) == 0:
            m = "0"

        while len(d) and d[0] == "0":
            d = d[1:]
        if len(d) == 0:
            d = "0"

        return ("{}-{}-{}".format(y, m, d))
