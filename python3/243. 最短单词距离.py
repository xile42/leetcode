class Solution:
    
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        idxs = list()
        marks = list()
        for idx, s in enumerate(wordsDict):
            if s == word1:
                idxs.append(idx)
                marks.append(0)
            elif s == word2:
                idxs.append(idx)
                marks.append(1)

        ans = float("inf")
        for idx in range(len(idxs)-1):
            if marks[idx] + marks[idx+1] == 1:
                ans = min(ans, idxs[idx+1] - idxs[idx])

        return ans
