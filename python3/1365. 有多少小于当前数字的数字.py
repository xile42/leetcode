class Solution:

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        c = Counter(nums)
        sn = sorted(set(nums))
        csn = [c[i] for i in sn]
        acc = list(accumulate(csn))
        d = dict()
        for i, j in zip(sn, acc):
            d[i] = j - c[i]

        return [d[i] for i in nums]
