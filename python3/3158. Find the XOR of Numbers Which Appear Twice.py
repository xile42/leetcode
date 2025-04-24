class Solution:

    def duplicateNumbersXOR(self, nums: List[int]) -> int:

        flag = 0
        ans = 0
        for num in nums:
            if (flag >> num) & 1:
                ans ^= num
            else:
                flag |= (1 << num)

        return ans
