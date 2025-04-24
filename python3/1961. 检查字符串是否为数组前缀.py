class Solution:

    def isPrefixString(self, s: str, words: List[str]) -> bool:

        ss = str()
        idx = 0
        while idx < len(words) and len(ss) != len(s):
            ss += words[idx]
            idx += 1

        return s == ss
