class Solution:
    
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        if len(sentence1) != len(sentence2):
            return False

        d = defaultdict(list)
        for i, j in similarPairs:
            d[i].append(j)
            d[j].append(i)

        for i in range(len(sentence1)):
            w1, w2 = sentence1[i], sentence2[i]
            if w1 == w2 or (w2 in d and w1 in d[w2]):
                continue
            else:
                return False

        return True
