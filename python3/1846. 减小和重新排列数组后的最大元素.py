class Solution:

    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()
        tar = 1
        for n in arr:
            if tar <= n:
                tar += 1
            else:
                continue

        return tar - 1
