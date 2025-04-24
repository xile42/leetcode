class Solution:

    def numberOfSpecialChars(self, word: str) -> int:

        sw = set(word)
        s = set()
        for c in sw:
            if c.lower() in sw and c.upper() in sw:
                s.add(c.lower())

        return len(s)
