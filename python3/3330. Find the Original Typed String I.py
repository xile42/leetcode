class Solution:

    def possibleStringCount(self, word: str) -> int:

        cnt = 1
        for idx in range(1, len(word)):
            if word[idx] == word[idx-1]:
                cnt += 1

        return cnt
