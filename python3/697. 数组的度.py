class Solution:

    def findShortestSubArray(self, nums: List[int]) -> int:

        c = Counter(nums)
        tar = max(c.values())
        tar_k = set()
        for k, v in c.items():
            if v == tar:
                tar_k.add(k)

        idxs = defaultdict(list)
        for i, n in enumerate(nums):
            if n in tar_k:
                idxs[n].append(i)

        ans = inf
        for k, v in idxs.items():
            ans = min(ans, v[-1] - v[0] + 1)

        return ans
