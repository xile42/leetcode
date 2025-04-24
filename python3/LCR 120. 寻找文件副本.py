class Solution:

    def findRepeatDocument(self, documents: List[int]) -> int:

        s = set()
        for i in documents:
            if i in s:
                return i
            s.add(i)
