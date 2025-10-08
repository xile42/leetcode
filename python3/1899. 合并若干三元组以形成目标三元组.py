class Solution:

    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        a, b, c = set(), set(), set()
        found = False
        for i, j, k in triplets:
            if i > target[0] or j > target[1] or k > target[2]:
                continue
            if i <= target[0] and j <= target[1] and k <= target[2]:
                found = True
            a.add(i)
            b.add(j)
            c.add(k)

        return found and target[0] in a and target[1] in b and target[2] in c
