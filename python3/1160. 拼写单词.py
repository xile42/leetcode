class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:

        result = 0
        s = set(chars)
        c = Counter(chars)
        for w in words:
            c1 = Counter(w)
            if len(set(c1.keys()) - s) == 0 and c1 <= c:
                result += len(w)

        return result
