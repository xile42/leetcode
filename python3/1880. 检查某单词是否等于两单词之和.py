class Solution:

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

        def f(s):

            return int("".join((str(ord(c) - ord("a")) for c in s)))

        return f(firstWord) + f(secondWord) == f(targetWord)
