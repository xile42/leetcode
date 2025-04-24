class Solution:

    def sortSentence(self, s: str) -> str:

        t = [[int(ss[-1]), ss[:-1]] for ss in s.split(" ")]
        t = sorted(t, key=lambda x: x[0])

        return " ".join([i[1] for i in t])
