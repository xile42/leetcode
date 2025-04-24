class Solution:

    def check(self, left, right):

        length_left, length_right = len(left), len(right)

        if length_left > length_right:
            return False

        if not right.startswith(left[::-1]):
            return False

        return True

    def shortestPalindrome(self, s: str) -> str:

        if len(s) <= 1:
            return s

        for idx in range(len(s)//2+1, -1, -1):

            if idx >= len(s):
                continue

            if self.check(s[:idx], s[idx+1:]):
                return s[idx+1:][::-1] + s[idx] + s[idx+1:]

            if self.check(s[:idx], s[idx:]):
                return s[idx:][::-1] + s[idx:]
