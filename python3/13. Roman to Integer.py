roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:

    def romanToInt(self, s: str) -> int:

        result = 0
        for x, y in pairwise(s):
            x, y = roman[x], roman[y]
            result += x if x >= y else -x

        return result + roman[s[-1]]
