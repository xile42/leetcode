class Solution:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        cnt = Counter()
        ans = 0
        for _, (a, b) in enumerate(dominoes):
            ans += cnt[(a, b)]
            if a != b:
                ans += cnt[(b, a)]
            cnt[(a, b)] += 1

        return ans
