class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:

        l = gcd(len(str1), len(str2))
        if str1[:l] == str2[:l] and str1 == str1[:l] * (len(str1) // l) and str2 == str2[:l] * (len(str2) // l):
            return str1[:l]

        return ""
