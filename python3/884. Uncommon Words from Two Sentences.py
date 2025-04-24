class Solution:

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        from collections import Counter

        counter1 = Counter(s1.split(" "))
        counter2 = Counter(s2.split(" "))

        results = list()
        for word, value in counter1.items():
            if value == 1 and word not in counter2:
                results.append(word)
        for word, value in counter2.items():
            if value == 1 and word not in counter1:
                results.append(word)

        return results
