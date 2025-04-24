class Solution:

    def vowelStrings(self, words: List[str], left: int, right: int) -> int:

        result = 0
        for word in words[left:right+1]:
            if word[0] in "aeiou" and word[-1] in "aeiou":
                result += 1

        return result
