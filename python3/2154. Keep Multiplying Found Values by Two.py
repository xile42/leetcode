class Solution:

    def findFinalValue(self, nums: List[int], original: int) -> int:

        count = defaultdict(int)
        for i in nums:
            if i in count:
                continue
            if i % original == 0:
                k = i // original
                if k.bit_count() == 1:
                    count[i] = 1

        while original in count:
            original <<= 1

        return original
