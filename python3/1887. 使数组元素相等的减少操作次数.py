class Solution:

    def reductionOperations(self, nums: List[int]) -> int:

        kvs = sorted(Counter(nums).items(), key=lambda x: x[0], reverse=True)
        ans = 0
        cur = 0
        for i in range(len(kvs) - 1):
            _, v = kvs[i]
            cur += v
            ans += cur

        return ans
