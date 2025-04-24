class Solution:

    def maxNumberOfApples(self, weight: List[int]) -> int:

        acc = list(accumulate(sorted(weight)))

        return bisect_right(acc, 5000)
