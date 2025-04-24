import re


class Solution:

    def removeVowels(self, s: str) -> str:

        return re.sub("[aeiou]", "", s)
