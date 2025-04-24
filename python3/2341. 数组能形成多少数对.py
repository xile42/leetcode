class Solution:

    def numberOfPairs(self, nums: List[int]) -> List[int]:

        vs = Counter(nums).values()
        ans1 = ans2 = 0
        for v in vs:
            ans1 += v // 2
            ans2 += v % 2

        return [ans1, ans2]
