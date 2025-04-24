class Solution:

    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        d = defaultdict(list)
        for i, w in enumerate(wordsDict):
            d[w].append(i)

        ans = inf
        same = word1 == word2
        n1, n2 = d[word1], d[word2]

        idx = jdx = 0
        while idx < len(n1) and jdx < len(n2):
            v1, v2 = n1[idx], n2[jdx]
            if same and idx == jdx:
                pass
            else:
                ans = min(ans, abs(v1 - v2))
            if v1 <= v2:
                idx += 1
            else:
                jdx += 1

        return ans
