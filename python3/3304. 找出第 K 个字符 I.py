import string


class Solution:

    def calculate(self, k):

        if k == 0:
            return self.word[0]

        if k - 1 < len(self.word):
            return self.word[k-1]

        round = 1
        while (1 << round) <= k:
            round += 1
        round -= 1

        if (1 << round) != k:
            return self.letter_shift[self.calculate(k - (1 << round))]
        else:
            return self.letter_shift[self.calculate(k // 2)]

    def kthCharacter(self, k: int) -> str:

        if k == 1:
            return "a"

        self.word = "abbcbccd"
        self.letter_shift = {string.ascii_lowercase[idx]: string.ascii_lowercase[idx+1] for idx in range(len(string.ascii_lowercase)-1)}
        self.letter_shift["z"] = "a"

        result = self.calculate(k)

        return result


if __name__ == '__main__':

    foo = Solution()
    result = foo.kthCharacter(16)
    print(result)
