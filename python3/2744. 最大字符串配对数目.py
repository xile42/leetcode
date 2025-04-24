class Solution:

    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        ans = 0
        s = set()
        for w in words:
            if w[::-1] in s:
                ans += 1
            s.add(w)

        return ans
