from functools import cmp_to_key


def f(a, b):

    i, j = a & 1, b & 1

    return i - j


class Solution:

    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        return sorted(nums, key=cmp_to_key(f))
