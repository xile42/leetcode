class Solution:

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        mx = max(candies)
        ans = list()
        for c in candies:
            ans.append(c + extraCandies >= mx)

        return ans
