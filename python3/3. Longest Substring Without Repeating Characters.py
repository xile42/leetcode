class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        occurence_map = dict()
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in occurence_map:
                left = max(left, occurence_map[s[right]] + 1)
            occurence_map[s[right]] = right
            max_length = max(max_length, right-left+1)

        return max_length
