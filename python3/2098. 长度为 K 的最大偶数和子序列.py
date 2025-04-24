class Solution:

    def largestEvenSum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        nums.sort()
        ans = sum(nums[-k:])
        if not ans & 1:
            return ans

        final_ans = -1

        cur_ans = ans
        found = False
        for i in range(-k, 0):
            if nums[i] & 1:
                cur_ans -= nums[i]
                found = True
                break
        if found:
            for i in range(-k - 1, -n - 1, -1):
                if not nums[i] & 1:
                    cur_ans += nums[i]
                    final_ans = max(final_ans, cur_ans)
                    break

        cur_ans = ans
        found = False
        for i in range(-k, 0):
            if not nums[i] & 1:
                cur_ans -= nums[i]
                found = True
                break
        if found:
            for i in range(-k - 1, -n - 1, -1):
                if nums[i] & 1:
                    cur_ans += nums[i]
                    final_ans = max(final_ans, cur_ans)
                    break


        return final_ans
