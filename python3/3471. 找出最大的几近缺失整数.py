class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        c = Counter()
        for i in range(len(nums)):
            arr = nums[i:i + k]
            if len(arr) < k:
                break
            for v in set(arr):
                c[v] += 1
        ans = list()
        for k, v in c.items():
            if v == 1:
                ans.append(k)

        return -1 if not ans else max(ans)