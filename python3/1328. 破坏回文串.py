class Solution:

    def breakPalindrome(self, palindrome: str) -> str:

        if len(palindrome) == 1:
            return ""

        if set(palindrome) == {"a"}:
            return palindrome[:-1] + "b"

        for i, c in enumerate(palindrome):
            if c != "a" and not (len(palindrome) & 1 and i == len(palindrome) // 2):
                return palindrome[:i] + "a" + palindrome[i + 1:]

        return palindrome[:-1] + "b"
