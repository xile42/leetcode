class Solution:

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def check(ns):

            ns.sort()
            if len(ns) == 1:
                return True
            d = ns[1] - ns[0]
            for i in range(2, len(ns)):
                if d != ns[i] - ns[i - 1]:
                    return False

            return True

        return [check(nums[i:j + 1]) for i, j in zip(l, r)]
