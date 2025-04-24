class Solution:

    def removeDigit(self, number: str, digit: str) -> str:

        return str(max(int(number[:i]+number[i+1:]) for i in range(len(number)) if number[i] == digit))
