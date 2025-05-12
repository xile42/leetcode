class Solution:

    def minimumRemoval(self, beans: List[int]) -> int:

        beans.sort()

        return sum(beans) - max((len(beans) - i) * beans[i] for i in range(len(beans)))
