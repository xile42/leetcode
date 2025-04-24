class Solution:

    def maximumEvenSplit(self, finalSum: int) -> List[int]:

        if finalSum & 1:
            return list()

        cur = 2
        ans = list()
        while finalSum >= cur:
            ans.append(cur)
            finalSum -= cur
            cur += 2

        if finalSum:
            ans[-1] += finalSum

        return ans
