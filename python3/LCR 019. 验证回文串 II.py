class Solution:

    def validPalindrome(self, s: str) -> bool:

        if s == s[::-1]:
            return True

        n = len(s)
        left, right = 0, n - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if (s[left+1:right+1] == s[left+1:right+1][::-1]) or (s[left:right] == s[left:right][::-1]):
                    return True
                return False
