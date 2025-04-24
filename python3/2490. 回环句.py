class Solution:

    def isCircularSentence(self, sentence: str) -> bool:

        ws = sentence.split(" ")

        return all(x[-1] == y[0] for x, y in pairwise(ws)) and ws[-1][-1] == ws[0][0]
