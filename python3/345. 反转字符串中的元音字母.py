class Solution:

    def reverseVowels(self, s: str) -> str:

        n = len(s)
        left, right = 0, n - 1
        yy = "aeiouAEIOU"
        s = list(s)

        while left < right:

            while left < n and s[left] not in yy:
                left += 1

            while right >= 0 and s[right] not in yy:
                right -= 1

            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)
        
