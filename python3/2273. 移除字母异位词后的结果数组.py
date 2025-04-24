class Solution:

    def removeAnagrams(self, words: List[str]) -> List[str]:

        return [w for i, w in enumerate(words) if i == 0 or Counter(words[i]) != Counter(words[i - 1])]
