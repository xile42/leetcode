import re


class Solution:

    def isPalindrome(self, s: str) -> bool:

        # \w不行，"_"也算\w
        s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

        return s == s[::-1]
