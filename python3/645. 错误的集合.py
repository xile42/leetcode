class Solution:

    def findErrorNums(self, nums: List[int]) -> List[int]:

        sn = sorted(nums)
        a, b = None, None

        for i, n in enumerate(sn):
            if i == 0 and n != 1:
                b = 1
                continue
            if n == sn[i - 1]:
                a = n
            if n == sn[i - 1] + 2:
                b = n - 1
            if a and b:
                break

        if b is None:
            b = len(nums)

        return [a, b]
