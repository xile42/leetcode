class Solution:

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        evens = [n for n in nums if not n & 1]
        odds = [n for n in nums if n & 1]

        return reduce(add, [[evens[i], odds[i]] for i in range(len(odds))])
