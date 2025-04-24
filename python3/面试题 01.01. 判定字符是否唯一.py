class Solution:

    def isUnique(self, astr: str) -> bool:

        return all(v == 1 for v in Counter(astr).values())
