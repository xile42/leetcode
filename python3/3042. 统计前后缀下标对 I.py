class Solution:

    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                w1, w2 = words[i], words[j]
                if w2.startswith(w1) and w2[::-1].startswith(w1[::-1]):
                    ans += 1

        return ans
