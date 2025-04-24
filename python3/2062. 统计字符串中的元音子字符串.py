class Solution:

    def countVowelSubstrings(self, word: str) -> int:

        return sum(sum(s == set("aeiou") for s in accumulate(map(set, word[i:]), or_)) for i in range(len(word)))
