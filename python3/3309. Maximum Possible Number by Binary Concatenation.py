class Solution:

    def maxGoodNumber(self, nums: List[int]) -> int:

        bs = [bin(num)[2:] for num in nums]
        bs = sorted(bs, reverse=True)

        results = list()
        for idx in range(3):
            for jdx in range(3):
                for kdx in range(3):
                    if idx != jdx and jdx != kdx and kdx != idx:
                        results.append(bs[idx]+bs[jdx]+bs[kdx])

        return max([int(i, 2) for i in results])
