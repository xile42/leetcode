class Solution:

    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        results = list()
        while s:
            results.append(s[:k])
            s = s[k:]
        while len(results[-1]) != k:
            results[-1] += fill

        return results
