class Solution:

    def scoreOfString(self, s: str) -> int:

        from string import ascii_lowercase

        char_map = {char: idx for idx, char in enumerate(ascii_lowercase)}

        nums = [char_map[i] for i in s]
        result = 0
        for idx in range(1, len(nums)):
            result += abs(nums[idx] - nums[idx-1])

        return result
