class Solution:

    def calculateTime(self, keyboard: str, word: str) -> int:

        d = {c: i for i, c in enumerate(keyboard)}
        vs = [d[c] for c in word]
        result = vs[0]
        for idx in range(1, len(vs)):
            result += abs(vs[idx] - vs[idx - 1])

        return result
