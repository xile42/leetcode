class Solution:

    def stringMatching(self, words: List[str]) -> List[str]:

        results = list()
        for w in words:
            for ww in words:
                if w != ww and w in ww:
                    results.append(w)
                    break

        return results
