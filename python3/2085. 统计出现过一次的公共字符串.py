class Solution:

    def countWords(self, words1: List[str], words2: List[str]) -> int:

        c1, c2 = Counter(words1), Counter(words2)

        return sum(c1[i] == 1 and c2[i] == 1 for i in c1.keys() | c2.keys())
