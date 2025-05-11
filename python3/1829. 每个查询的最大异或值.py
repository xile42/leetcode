class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:

        ans = list()
        cur = 0
        for v in nums:
            cur ^= v
            mask = 0
            print(v, cur)
            for i in range(maximumBit):
                if (cur >> i) & 1 == 0:
                    mask |= 1 << i
            ans.append(mask)

        return ans[::-1]
