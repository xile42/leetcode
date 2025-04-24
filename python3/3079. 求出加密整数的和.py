class Solution:

    def sumOfEncryptedInt(self, nums: List[int]) -> int:

        ans = 0
        for n in nums:
            sn = str(n)
            ans += int(str(max(list(map(int, sn)))) * len(sn))

        return ans
