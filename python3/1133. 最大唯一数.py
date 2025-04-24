class Solution:

    def largestUniqueNumber(self, nums: List[int]) -> int:

        s1 = set()
        s2 = set()
        for n in nums:
            if n not in s2:
                if n in s1:
                    s1.remove(n)
                    s2.add(n)
                else:
                    s1.add(n)

        return -1 if not len(s1) else max(s1)
