class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        return s != t and Counter(s) == Counter(t)
