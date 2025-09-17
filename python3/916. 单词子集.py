class Solution:

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        tar = Counter()
        for w in words2:
            tar |= Counter(w)

        ans = list()
        for w in words1:
            if Counter(w) >= tar:
                ans.append(w)

        return ans
