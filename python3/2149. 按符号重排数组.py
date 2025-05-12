class Solution:

    def rearrangeArray(self, nums: List[int]) -> List[int]:

        pos = [n for n in nums if n > 0]
        neg = [n for n in nums if n < 0]

        # return reduce(add, map(list, zip(pos, neg)))

        ans = list()
        for a, b in zip(pos, neg):
            ans += [a, b]

        return ans
