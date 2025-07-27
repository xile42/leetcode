class Solution:

    def countOddLetters(self, n: int) -> int:

        d = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        c = Counter("".join(d[int(i)] for i in str(n)))

        return sum(1 for v in c.values() if v % 2 == 1)
