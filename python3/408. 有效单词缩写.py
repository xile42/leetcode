class Solution:

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        l = len(word)
        cur = 0
        j = 0
        for i in range(len(abbr)):
            c = abbr[i]
            if c.isdigit():
                if c == "0" and cur == 0:
                    return False
                else:
                    cur *= 10
                    cur += int(c)
            else:
                j += cur
                cur = 0
                if j >= len(word) or word[j] != c:
                    return False
                j += 1

        return l == j + cur
