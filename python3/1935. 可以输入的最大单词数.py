class Solution:

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        s = set(brokenLetters)
        ans = 0
        for w in text.split(" "):
            if len(set(w) & s) == 0:
                ans += 1

        return ans
