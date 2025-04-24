class Solution:

    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:

        results = list()
        for w in words:
            for i in range(len(text) - len(w) + 1):
                if text[i:i+len(w)] == w:
                    results.append([i, i+len(w)-1])

        return sorted(results)
