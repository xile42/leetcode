class Solution:

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        sa = sorted(arr)

        return len(set([sa[i] - sa[i - 1] for i in range(1, len(sa))])) == 1
