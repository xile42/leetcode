class Solution:

    def mostFrequentEven(self, nums: List[int]) -> int:

        ns = [i for i in nums if i & 1 == 0]
        sns = sorted([[v, -k] for k, v in Counter(ns).items()], reverse=True)

        return -1 if len(sns) == 0 else -sns[0][-1]        
