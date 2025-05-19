class Solution:

    def doesAliceWin(self, s: str) -> bool:

        c = Counter(s)
        n = c["a"] + c["e"] + c["i"] + c["o"] + c["u"]

        if n == 0:
            return False
        return True
