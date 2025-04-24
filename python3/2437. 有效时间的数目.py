class Solution:

    def countTime(self, time: str) -> int:

        a, b, c, d = time[0:2] + time[3:]

        if a == b and a == "?":
            x = 24
        elif a != "?" and b != "?":
            x = 1
        elif a == "?":
            x = 3 if b <= "3" else 2
        elif b == "?":
            x = 4 if a == "2" else 10

        if c == d and c == "?":
            y = 60
        elif c != "?" and d != "?":
            y = 1
        elif c == "?":
            y = 6
        elif d == "?":
            y = 10

        return x * y
