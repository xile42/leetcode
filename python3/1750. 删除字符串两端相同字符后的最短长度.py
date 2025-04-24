class Solution:

    def minimumLength(self, s: str) -> int:

        left = 0
        right = len(s) - 1
        while left <= right:
            if left == right:
                break
            if s[left] != s[right]:
                break
            c = s[left]
            while left <= right and s[left] == c:
                left += 1
            while left <= right and s[right] == c:
                right -= 1

        return len(s) - (len(s) - 1 - right + left)
