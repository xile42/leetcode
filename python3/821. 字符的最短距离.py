class Solution:

    def shortestToChar(self, s: str, c: str) -> List[int]:

        valid = [idx for idx in range(len(s)) if s[idx] == c]
        results = list()
        for idx in range(len(s)):
            results.append(min(abs(jdx - idx) for jdx in valid))

        return results
