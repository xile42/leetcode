class Solution:

    def reverseWords(self, s: List[str]) -> None:

        for i, c in enumerate(list(" ".join([w[::-1] for w in "".join(s).split(" ")]))[::-1]):
            s[i] = c    
