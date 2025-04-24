class Solution:

    def sortByBits(self, arr: List[int]) -> List[int]:

        ns = [[n.bit_count(), n] for n in arr]

        return [i[1] for i in sorted(ns)]
