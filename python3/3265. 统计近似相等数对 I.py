class Solution:

    def countPairs(self, nums: List[int]) -> int:

        def check(s1, s2):

            l = max(len(s1), len(s2))
            s1 = "0" * (l - len(s1)) + s1
            s2 = "0" * (l - len(s2)) + s2
            c1 = Counter(s1)
            c2 = Counter(s2)
            dis = sum(i != j for i, j in zip(s1, s2))

            return dis == 0 or dis == 2 and c1 == c2

        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                ans += check(str(nums[i]), str(nums[j]))

        return ans
