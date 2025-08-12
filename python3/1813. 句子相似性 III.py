class Solution:

    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        w1 = sentence1.split()
        w2 = sentence2.split()
        n1, n2 = len(w1), len(w2)

        if n1 == n2:
            return w1 == w2

        if n1 > n2:
            w1, w2 = w2, w1
            n1, n2 = n2, n1

        i = 0
        while i < n1 and w1[i] == w2[i]:
            i += 1

        j = -1
        while j >= -n1 and w1[j] == w2[j]:
            j -= 1

        return i + abs(j) - 1 >= n1
