class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        allowed_set = set(allowed)
        result = 0
        for word in words:
            word_set = set(word)
            if len(word_set - allowed_set) == 0:
                result += 1

        return result
