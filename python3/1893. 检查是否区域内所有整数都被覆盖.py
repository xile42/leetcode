class Solution:

    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        diff = [0] * 52
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1
        acc = list(accumulate(diff))

        return all(acc[i] != 0 for i in range(left, right + 1))
