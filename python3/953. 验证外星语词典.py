from functools import cmp_to_key


class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:

        d = {c: i for i, c in enumerate(order)}

        def f(a, b):

            if a == b:
                return 0
            
            if b.startswith(a):
                return -1

            if a.startswith(b):
                return 1

            for i in range(min(len(a), len(b))):
                v1 = d[a[i]]
                v2 = d[b[i]]
                if v1 != v2:
                    return v1 - v2

        sorted_words = sorted(words, key=cmp_to_key(f))

        return sorted_words == words
