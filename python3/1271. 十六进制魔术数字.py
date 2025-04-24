class Solution:

    def toHexspeak(self, num: str) -> str:

        s = hex(int(num))[2:]
        s = s.upper().replace("0", "O").replace("1", "I")

        return s if s.isalpha() else "ERROR"
