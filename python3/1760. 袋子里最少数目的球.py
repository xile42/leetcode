class Solution:

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def check(tar):

            chance = maxOperations
            for v in nums:
                if v <= tar:
                    continue
                elif chance == 0:
                    return False
                else:
                    chance -= ceil(v / tar) - 1
                    if chance < 0:
                        return False

            return True

        nums.sort()
        left = 1
        right = nums[-1]
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
