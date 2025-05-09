class Solution:

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        s = {tops[0], bottoms[0]}
        for i in range(1, len(tops)):
            s &= {tops[i], bottoms[i]}
            if not s:
                return -1

        ans = inf
        for tar in s:
            ans = min(ans, sum(i != tar for i in tops), sum(i != tar for i in bottoms))

        return ans
