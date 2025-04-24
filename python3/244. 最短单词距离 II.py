class WordDistance:

    def __init__(self, wordsDict: List[str]):

        self.d = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.d[w].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:

        n1, n2 = self.d[word1], self.d[word2]
        ans = inf
        for i in n1:
            for j in n2:
                ans = min(ans, abs(i - j))

        return ans


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
