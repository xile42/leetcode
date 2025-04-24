class Solution:

    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:

        kb = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = words
        for i, v in enumerate(num):
            for word in words:
                if not word[i] in kb[v]:
                    ans.remove(word)

        return ans
