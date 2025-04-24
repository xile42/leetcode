class Solution:

    def distance(self, nums: List[int]) -> List[int]:

        d = defaultdict(list)
        for i, v in enumerate(nums):
            d[v].append(i)

        ans = [0] * len(nums)
        for v in d:
            acc = list(accumulate(d[v]))
            for idx, i in enumerate(d[v]):
                left = 0 if idx == 0 else idx * i - acc[idx - 1]
                right = 0 if idx == len(d[v]) - 1 else acc[-1] - acc[idx] - (len(d[v]) - 1 - idx) * i
                ans[i] = left + right

        return ans
