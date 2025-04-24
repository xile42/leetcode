class Solution:

    def reverseWords(self, s: str) -> str:

        ws = s.split(" ")
        ws = [i for i in ws if len(i) > 0]

        return " ".join(ws[::-1])
