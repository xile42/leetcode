import re


class Solution:

    def countValidWords(self, sentence: str) -> int:

        ws = re.split(r"\s+", sentence)
        ans = 0
        for w in ws:
            if w and re.match(r"[a-z]*([a-z]\-[a-z])?[a-z]*[!.,]?$", w):
                ans += 1

        return ans
