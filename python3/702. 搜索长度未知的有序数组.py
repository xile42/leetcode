# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:

    def search(self, reader: 'ArrayReader', target: int) -> int:

        left = 0
        right = pow(10, 4) + 1
        na_value = (1 << 31) - 1
        while left <= right:
            mid = left + (right - left) // 2
            v = reader.get(mid)
            if v == target:
                return mid
            elif v == na_value or v > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
