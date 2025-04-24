class Solution:

    def reverseMessage(self, message: str) -> str:

        ws = message.split(" ")
        ws = [i for i in ws if len(i) > 0]

        return " ".join(ws[::-1])
