class Solution:

    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        ans = list()
        idx = 0
        for c, ite in groupby(groups):
            l = len(list(ite))
            ans.append(words[idx])
            idx += l

        return ans
