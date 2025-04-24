import string


class Solution:
    
    def reverseOnlyLetters(self, s: str) -> str:

        n = len(s)
        valid = string.ascii_lowercase + string.ascii_uppercase
        left, right = 0, n - 1
        s = list(s)

        while left < right:
            while left < n and s[left] not in valid:
                left += 1
            while right >= 0 and s[right] not in valid:
                right -= 1
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)
        
