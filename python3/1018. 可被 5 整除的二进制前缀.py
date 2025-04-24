class Solution:

    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:

        s = str()
        ans = list()
        for c in nums:
            s += str(c)
            ans.append(True if int(s, 2) % 5 == 0 else False)

        return ans
