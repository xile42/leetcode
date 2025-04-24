class Solution:

    def isValid(self, word: str) -> bool:

        if len(word) < 3:
            return False

        if len(set(word) - set(string.ascii_letters + string.digits)) != 0:
            return False

        word = word.lower()

        if len(set(word) & set("aeiou")) == 0 or len(set(word) - set("aeiou0123456789")) == 0:
            return False

        return True
