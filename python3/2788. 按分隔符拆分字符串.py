class Solution:

    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:

        ans = list()
        for w in words:
            ans += w.split(separator)
        ans = [i for i in ans if len(i)]

        return ans
