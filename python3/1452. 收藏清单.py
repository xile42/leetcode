class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:

        ans = list()

        for i, words in enumerate(favoriteCompanies):
            words = set(words)
            for j, other_words in enumerate(favoriteCompanies):
                other_words = set(other_words)
                if i != j and words.issubset(other_words):
                    break
            else:
                ans.append(i)

        return ans
