class Solution:

    def findLucky(self, arr: List[int]) -> int:

        c = Counter(arr)

        for k in sorted(c.keys(), reverse=True):
            if k == c[k]:
                return k

        return -1
