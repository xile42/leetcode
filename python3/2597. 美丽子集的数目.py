class Solution:

    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        nums.sort()
        ans = set()

        def f(idx, s, mask):

            nonlocal ans
            if idx >= len(nums):
                if mask:
                    ans.add(mask)
                return

            f(idx + 1, s, mask)
            if nums[idx] - k not in s:
                f(idx + 1, s | {nums[idx]}, mask | 1 << (idx))

        f(0, set(), 0)

        return len(ans)
