class Solution:

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        cnt = Counter()
        for i, c in enumerate(words):
            if c[0] in "aeiou" and c[-1] in "aeiou":
                cnt[i] = cnt[i - 1] + 1
            else:
                cnt[i] = cnt[i - 1]

        ans = list()
        for l, r in queries:
            ans.append(cnt[r] - cnt[l - 1])

        return ans
