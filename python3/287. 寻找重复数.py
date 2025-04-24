class Solution:

    def findDuplicate(self, nums: List[int]) -> int:

        slow = 0
        fast = 0

        while True:
            # fast 前进两次，slow 前进一次
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
            if slow == fast:
                break

        # ptr == slow 时说明检测到重复元素，两个重复元素同时指向环的入口。
        ptr = 0
        while ptr != slow:
            ptr = nums[ptr]
            slow = nums[slow]

        return ptr
